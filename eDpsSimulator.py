"""
Licensing note: AGPL does not apply to the spellDb.json, as Nexon is the owner of this information. However, I am asserting that this is a fair use of that information.

    Spell Rotation Simulator
    Copyright (C) 2026 Kero; Free Software Foundation

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import csv
import math
import random
import json
from concurrent.futures import ThreadPoolExecutor
import copy
import pandas as pd


N_DEBUG = False
eventLogAnchor = "[{Timestamp}]->[{Timestamp2}]\t{SpellName}\t{Activity}"

# Genetic Algorithm Parameters
GA_CULL_PERCENT =               0.50 # Rank rotations by DPS, drop the bottom half, and start breeding
GA_GLOBAL_MUTATION_RATE =       0.001 # For each spell in a rotation: random chance to any known spell
GA_FITNESS_FUNCTION =           lambda fitnessTarget,fitness: fitnessTarget - fitness # Can change to any error-penalizing function you want (e.g. squared error)
GA_FOREST_SIZE =                10        # How many rotations to work with
GA_GRADBOOST_AUTOCULL =         44.55        # Automatically cull & replace rotations falling below this DPS threshold (ideally 90% of best known rotation)
GA_FITNESS_TARGET =             120.00      # Instantly terminate the simulation upon reaching this value (may be impossible)

# Simulation Parameters
SIM_TARGETS =               5           # Even in SIM, FoE! https://youtu.be/dB_PVPyn6n8
SIM_ADVANCE_RETARD =        1.00        # Globally advance or retard spell timings (e.g. +10% attack speed => 1.10)
SIM_TIMING_EPSILON =        10.00       # Timing step for simulation in milliseconds (i.e. dX in Calculus)
SIM_DROP_CAST_CHANCE =      0.01        # Chance for spell to whiff
SIM_RUNTIME =               600000.00    # How long to simulate the rotation
SIM_ROTATION_SIZE =         1000        # How deep to generate a rotation

"""
SpellDB Fields
SpellName
Potency             Effective base damage (i.e. base damage * probability)
Timing              Time from start of cast to hit on enemy (usually 2-3 seconds)
Interdicting        Whether or not the cast is active
TargetIdsAffected   Some effects hit "certain targets", while "avoiding others"; some effects are mutually exclusive. Fixed enemy IDs are used to keep track of this.
SecondaryEffect     Secondary spell effects, as spells themselves
Unique              Whether or not the spell needs to wear off before re-applying
"""

# TODO: evaluate rotations ('the meat' of the programming)

spellDatabaseFile = open('./spellDb.json', 'r')
spellDatabase = json.load(spellDatabaseFile)

def generateRotation():
    nRotation = []
    for i in range(0, SIM_ROTATION_SIZE):
        nRotation.append(copy.deepcopy(random.choice(spellDatabase)))
    return nRotation

def generateRotations(count=GA_FOREST_SIZE):
    allRotations = []
    with ThreadPoolExecutor() as executor:
        jobs = []
        for i in range(0,count):
            jobs.append(executor.submit(generateRotation))
        for job in jobs:
            allRotations.append(job.result())
    return allRotations

def blendRotations(mother, father):
    nChild = []
    for motherSpell,fatherSpell in zip(mother,father):
        nChild.append(random.choice([motherSpell,fatherSpell]))
    return nChild

def simulateRotation(rotation):
    currentTime =   0.00
    terminalTime =  SIM_RUNTIME

    damageAttributions = pd.DataFrame(columns=['Timestamp', 'SpellName', 'Damage'])
    rotationPerformed = []

    interdictedTill = -0.01
    activeSpells = []

    while currentTime < terminalTime:
        spellsToRemove = []
        for spell in activeSpells:
            spell['Timing'][1] -= SIM_TIMING_EPSILON
            if spell['Timing'][1] <= 0.00:
                    #damageAttributions.append( (currentTime, spell['SpellName'], spell['Potency']*min(SIM_TARGETS,len(spell['TargetIdsAffected']))) )
                    damageAttributions.loc[len(damageAttributions)] = {'Timestamp': currentTime, 'SpellName': spell['SpellName'], 'Damage': spell['Potency']*min(SIM_TARGETS,len(spell['TargetIdsAffected']))}
                    spellsToRemove.append(spell)
        for spellToRemove in spellsToRemove: # remove() does not work while iterating on the parent list
            activeSpells.remove(spellToRemove)
            print(eventLogAnchor.format(Timestamp=currentTime,Activity='Lapsed',SpellName=spellToRemove['SpellName'],Timestamp2='NULL')) if N_DEBUG else ''
        spellsToRemove = [] # Clear it out

        if currentTime <= interdictedTill: # Simulating animation lock
            currentTime += SIM_TIMING_EPSILON
            continue
        else:
            spell = rotation.pop(0)
            rotationPerformed.append(copy.deepcopy(spell))
            if spell['Interdicting'] == True:
                interdictedTill = currentTime + spell['Timing'][1]
            activeSpells.append(spell)
            print(eventLogAnchor.format(Timestamp=currentTime,Activity='Activated',SpellName=spell['SpellName'],Timestamp2=currentTime+spell['Timing'][1])) if N_DEBUG else ''

            for sSpell in spell['SecondaryEffect']:
                sSpell['Timing'] = [ 0.00, spell['Timing'][1] + sSpell['TimingOffset'][1] ]

                suppress = False
                if sSpell['Unique'] == True:
                    for oSpell in activeSpells:
                        if oSpell['SpellName'] == sSpell['SpellName']: suppress = True
                if not suppress: 
                    activeSpells.append(sSpell)
                    print(eventLogAnchor.format(Timestamp=currentTime,Activity='Activated',SpellName=sSpell['SpellName'],Timestamp2=currentTime+sSpell['Timing'][1])) if N_DEBUG else ''
                else:
                    print(eventLogAnchor.format(Timestamp=currentTime,Activity='SUPPRESSED',SpellName=sSpell['SpellName'],Timestamp2='NULL')) if N_DEBUG else ''
                
        currentTime += SIM_TIMING_EPSILON

    return (damageAttributions, rotationPerformed)

def analyzeRotation(damageAttributions, rotationPerformed):
    totalDamageWithAttribution = damageAttributions.groupby('SpellName')['Damage'].sum().reset_index().values.tolist()
    totalGeneralDamage = damageAttributions.sum(numeric_only=True).drop('Timestamp')
    totalGeneralDps = (SIM_ADVANCE_RETARD * totalGeneralDamage['Damage']) / (SIM_RUNTIME / 1000)

    fitness = GA_FITNESS_FUNCTION(GA_FITNESS_TARGET, totalGeneralDps)

    prettyPrintRotationPerformed = []
    for spell in rotationPerformed:
        prettyPrintRotationPerformed.append(spell['SpellName'])
    return (fitness, totalDamageWithAttribution, rotationPerformed, prettyPrintRotationPerformed)

forest = generateRotations()
simResults = []
dpsAnalysis = []

with ThreadPoolExecutor() as simExecutor:
    jobs = []
    for i in range(0,len(forest)):
        jobs.append(simExecutor.submit(simulateRotation, forest[i]))
    for job in jobs:
        simResults.append(job.result())

with ThreadPoolExecutor() as dpsExecutor:
    jobs = []
    for i in range(0,len(simResults)):
        jobs.append(dpsExecutor.submit(analyzeRotation, *simResults[i]))
    for job in jobs:
        dpsAnalysis.append(job.result())

dpsAnalysis = list( filter(lambda x: x[0] > GA_GRADBOOST_AUTOCULL, dpsAnalysis) )
dpsAnalysis.sort(key=lambda x: x[0], reverse=True)
dpsAnalysis = dpsAnalysis[0:int(len(dpsAnalysis)*GA_CULL_PERCENT)]

# mutate here

# blend here

# continue cycle here

pass