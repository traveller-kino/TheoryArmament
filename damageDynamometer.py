import csv
import math
import random
import json
from concurrent.futures import ThreadPoolExecutor
import copy
import pandas as pd
import pickle
import bz2
import time

spellDatabaseFile = open('./spellDb.json', 'r')
spellDatabase = json.load(spellDatabaseFile)
# Note need to stop editing spells directly, and use an associative array for tracking time expirations

# Simulation Parameters
SIM_TARGETS =               5           # Even in SIM, FoE! https://youtu.be/dB_PVPyn6n8
SIM_ADVANCE_RETARD =        1.00        # Globally advance or retard spell timings (e.g. +10% attack speed => 1.10)
SIM_TIMING_EPSILON =        10.00       # Timing step for simulation in milliseconds (i.e. dX in Calculus)
SIM_DROP_CAST_CHANCE =      0.01        # Chance for spell to whiff
SIM_RUNTIME =               600000.00    # How long to simulate the rotation

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


pass