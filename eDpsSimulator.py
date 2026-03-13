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

# Genetic Algorithm Parameters
GA_CULL_PERCENT =               0.50 # Rank rotations by DPS, drop the bottom half, and start breeding
GA_GLOBAL_MUTATION_RATE =       0.001 # For each spell in a rotation: random chance to any known spell
GA_FITNESS_FUNCTION =           lambda fitnessTarget,fitness: fitnessTarget - fitness # Can change to any error-penalizing function you want (e.g. squared error)
GA_CROSSOVER_FUNCTION =         lambda motherSpell,fatherSpell: random.choice([motherSpell, fatherSpell]) # Crossover: for rotation slots in common, keep. Otherwise, randomly choose between the two.

# Simulation Parameters
SIM_TARGETS =           5           # Even in SIM, FoE! https://youtu.be/dB_PVPyn6n8
SIM_ADVANCE_RETARD =    1.00        # Globally advance or retard spell timings (e.g. +10% attack speed => 1.10)
SIM_TIMING_EPSILON =    10.00       # Timing step for simulation in milliseconds (i.e. dX in Calculus)
SIM_DROP_CAST_CHANCE =  0.01        # Chance for spell to whiff

"""
SpellDB Fields
SpellName
Potency             Effective base damage (i.e. base damage * probability)
Timing              Time from start of cast to hit on enemy (usually 2-3 seconds)
Interdicting        Whether or not the cast is active
TargetIdsAffected   Some effects hit "certain targets", while "avoiding others"; some effects are mutually exclusive. Fixed enemy IDs are used to keep track of this.
SecondaryEffect     Secondary spell effects, as spells themselves
"""

# TODO: randomly generate rotation
# TODO: blend rotations via crossover
# TODO: evaluate rotations ('the meat' of the programming)

spellDatabaseFile = open('./spellDb.json', 'r')
spellDatabase = json.load(spellDatabaseFile)

print('Dynamometer has started running...')
print(str(GA_CROSSOVER_FUNCTION('poison brace', 'fire arrow')))

