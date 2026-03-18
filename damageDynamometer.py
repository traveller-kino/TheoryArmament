import csv
import random
import json
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

"""
SpellDB Fields
SpellName
Potency             Effective base damage (i.e. base damage * probability)
Timing              Time from start of cast to hit on enemy (usually 2-3 seconds)
Interdicting        Whether or not the cast is active
TargetIdsAffected   Some effects hit "certain targets", while "avoiding others"; some effects are mutually exclusive. Fixed enemy IDs are used to keep track of this.
SecondaryEffect     Secondary spell effects, as spells
Unique              Whether or not the spell needs to wear off before re-applying
"""
N_DEBUG = False
eventLogAnchor = "[{Timestamp}]->[{Timestamp2}]\t{SpellName}\t{Activity}"
N_ALLOW_GUI = True

spellDatabaseFile = open('./spellDb.json', 'r')
spellDatabase = json.load(spellDatabaseFile)
spellIndex = {}
for spell in spellDatabase:
    spellIndex[spell['SpellName']] = spell
dotIndex = {}
for spell in spellDatabase:
    if spell.get('SecondaryEffect') is None: break
    
    for sSpell in spell.get('SecondaryEffect'):
        if sSpell.get('GroupId'):
            dot = sSpell
            if dotIndex.get(sSpell.get('GroupId')):
                dotIndex[sSpell.get('GroupId')].append(dot)
            else: dotIndex[sSpell.get('GroupId')] = [dot]

# Simulation Parameters
SIM_TARGETS =               5           # Even in SIM, FoE! https://youtu.be/dB_PVPyn6n8
SIM_ADVANCE_RETARD =        1.00        # Globally advance or retard spell timings (e.g. +10% attack speed => 1.10)
SIM_TIMING_EPSILON =        1.000       # Timing step for simulation in milliseconds (i.e. dX in Calculus)
SIM_DROP_CAST_CHANCE =      0.01        # Chance for spell to whiff
SIM_RUNTIME =               300000.00    # How long to simulate the rotation

def readRotation(filename):
    rotation = []
    theFile = open(filename, 'r')
    csvRotation = csv.reader(theFile)
    for row in csvRotation: # Note: row is an array of comma seperated values (so, row[0] is needed)
        rotation.append(spellIndex[row[0]])
    theFile.close()
    return rotation

# NOTE: need to stop editing spells directly, and use an associative array for tracking time expirations
# "new" timing code
    # add active spell to queue | activeSpells = []
    # New spells are always APPENDED to activeSpells
    # add timing queue | spellTimers = []
    # ..., so order is preserved
    # this way, activeSpells and spellTimers indices always 'stay with each other'
def simulateRotation(rotation):
    currentTime =   0.00
    terminalTime =  SIM_RUNTIME

    damageAttributions = pd.DataFrame(columns=['Timestamp', 'SpellName', 'Damage'])

    interdictedTill = -0.01
    activeSpells = []
    spellTimers = []

    while currentTime < terminalTime:
        spellsToRemove = []
        timersToRemove = []
        #for spell, timer in zip(activeSpells, spellTimers): # change to zip
        for i in range(0, len(activeSpells)):
            spellTimers[i] -= SIM_TIMING_EPSILON
            if  spellTimers[i] <= 0.00:
                    damageAttributions.loc[len(damageAttributions)] = {'Timestamp': currentTime, 'SpellName': activeSpells[i]['SpellName'], 'Damage': activeSpells[i]['Potency']*min(SIM_TARGETS,len(activeSpells[i]['TargetIdsAffected']))}
                    spellsToRemove.append(activeSpells[i])
                    timersToRemove.append(spellTimers[i])
        for i in range(0,len(spellsToRemove)):
            activeSpells.remove(spellsToRemove[i])
            spellTimers.remove(timersToRemove[i])
            print(eventLogAnchor.format(Timestamp=currentTime,Activity='Lapsed',SpellName=spellsToRemove[i]['SpellName'],Timestamp2='NULL')) if N_DEBUG else ''
        spellsToRemove = []
        timersToRemove = []

        if currentTime <= interdictedTill: # Simulating animation lock
            currentTime += SIM_TIMING_EPSILON
            continue
        else:
            if random.uniform(0.00, 1.00) < SIM_DROP_CAST_CHANCE: 
                interdictedTill = max(interdictedTill, currentTime + 1500)
                print(eventLogAnchor.format(Timestamp=currentTime,Activity='DROPPED',SpellName='NULL',Timestamp2=interdictedTill)) if N_DEBUG else ''
                continue

            spell = rotation.pop(0)
            if spell['Interdicting'] == True:
                interdictedTill = currentTime + spell['Timing'][1]
            activeSpells.append(spell)
            spellTimers.append(spell['Timing'][1])
            print(eventLogAnchor.format(Timestamp=currentTime,Activity='Activated',SpellName=spell['SpellName'],Timestamp2=currentTime+spell['Timing'][1])) if N_DEBUG else ''

            frozenActiveSpells = activeSpells.copy() # Need copy or else latent effects will fail to apply beyond first tick
            if spell.get('SecondaryEffect') == None: continue
            for sSpell in spell.get('SecondaryEffect'):
                sSpell['Timing'] = [ 0.00, spell['Timing'][1] + sSpell['TimingOffset'][1] ]
                
                suppress = False
                if sSpell['Unique'] == True: # if resettable, re-apply by group ID, otherwise, ignore
                    for oSpell in frozenActiveSpells:
                        if not oSpell.get('GroupId'): continue
                        else: 
                            if oSpell.get('GroupId') == sSpell.get('GroupId'): suppress = True
                if not suppress: 
                    activeSpells.append(sSpell)
                    spellTimers.append(sSpell['Timing'][1])
                    print(eventLogAnchor.format(Timestamp=currentTime,Activity='Applied',SpellName=sSpell['SpellName'],Timestamp2=currentTime+sSpell['Timing'][1])) if N_DEBUG else ''
                else:
                    # TODO: add DoT resetting
                    print(eventLogAnchor.format(Timestamp=currentTime,Activity='RESET',SpellName=sSpell['SpellName'],Timestamp2='NULL')) if N_DEBUG else ''
                
        currentTime += SIM_TIMING_EPSILON
    return damageAttributions

def runDyno(filePath, friendlyName):
    a = readRotation(filePath)
    b = simulateRotation(a)

    totalDamageWithAttribution = b.groupby('SpellName')['Damage'].sum().reset_index().values.tolist()
    totalGeneralDamage = b.sum(numeric_only=True).drop('Timestamp')
    totalGeneralDps = (SIM_ADVANCE_RETARD * totalGeneralDamage) / (SIM_RUNTIME / 1000)

    b['Timestamp'] = pd.to_datetime(b['Timestamp'],unit='ms')
    b['Cumulative Damage'] = b.groupby("SpellName")['Damage'].cumsum()
    for spell_name, entry_data in b.groupby("SpellName"):
        plt.plot(entry_data['Timestamp'], entry_data['Cumulative Damage'], label=spell_name)
    plt.plot(b['Timestamp'], b['Damage'].cumsum(), label='Total')
    #b.plot(x='Timestamp', y='Cumulative Damage', kind='line')
    plt.legend(title="Damage Source")
    plt.title("Dynamometer Output for {n} Targets\nStrategy={strategy}\nTotal = {total}\nDPS = {dps}".format(n=SIM_TARGETS,total=totalGeneralDamage.values[0],dps=totalGeneralDps.values[0],strategy=friendlyName))
    plt.xlabel("Simulator Time", fontsize=12)
    plt.ylabel("Cumulative Damage", fontsize=12)
    plt.grid(True, alpha=0.5)
    if N_ALLOW_GUI: plt.show()
    print(friendlyName + '\t\t' + str(totalGeneralDps.values[0]))
    return

for rotationFile in os.listdir('./rotationSpecimens'):
    folderAnchor = './rotationSpecimens/' # be careful of path traversal vulns
    fileName = folderAnchor + rotationFile
    runDyno(fileName, rotationFile[:-4])