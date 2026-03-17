# Rotation simulation (currently for F/P Mages)
Note: this is not for "MapleStory at home" ;) (not that you'd roll F/P anyway), this is for the upcoming Classic World, with the information we know.


Current simulator results of interest:
| Pattern / Mobs Targeted : DPS | 1           | 2            | 3            | 4        | 5             |   | AVG            | MAX           |   | AVG MP/S     | DMG/MP               |
|-------------------------------|-------------|--------------|--------------|----------|---------------|---|----------------|---------------|---|--------------|----------------------|
| **AB**                        | **27.4416** | **48.1979**  | **68.96354** | **74.2** | **84.4083**   |   | **60.642268**  | **84.4083**   |   | **11.6666**  | **5.19793838821936** |
| ABBB                          | 25.34895    | 46.927       | 67.93958     | 73.4875  | 78.9447916    |   | 58.52956432    | 78.9447916    |   | 10.8333      | 5.40274563798658     |
| BAA                           | 26.95       | 45.1         | 63.25        | 72       | 81.95         |   | 57.85          | 81.95         |   | 12.2222      | 4.73319042398259     |
| BAAA                          | 26.735416   | 44.160416    | 61.3072916   | 71.75    | 82.2208       |   | 57.23478472    | 82.2208       |   | 12.5         | 4.5787827776         |
| ABx4                          | 23.633      | 44.6         | 65.4666      | 69.4     | 73.2333       |   | 55.26658       | 73.2333       |   | 10.6666      | 5.18127425796411     |
| ABB                           | 23.815625   | 43.25        | 62.675       | 67.7625  | 72.878        |   | 54.076225      | 72.878        |   | 11.1111      | 4.86686511686512     |
| **Poison Brace (A)**          | **26.625**  | **39.62708** | **52.96354** | **66.9** | **79.467708** |   | **53.1166656** | **79.467708** |   | **13.3333**  | **3.9837598793997**  |
| **Fire Arrow (B)**            | **21.4666** | **42.9333**  | **63.7**     | **64.4** | **64.3**      |   | **51.35998**   | **64.4**      |   | **10**       | **5.135998**         |
| **Eco Mode**                  | **15.5833** | **27.24375** | **40.5**     | **45.6** | **50.746875** |   | **35.934785**  | **50.746875** |   | **6.363636** | **5.64689510839401** |

*Figures are in base damage per second (internally called "Potency")*

Special note: "Eco Mode" is casting Poison Brace & Fire Arrow, and waiting for the poison DoT to expire. While it isn't particularly good, it's interesting knowing it isn't laughably low.

Alternating Poison Brace & Fire Arrow results in the highest DPS. This makes sense, especially in a "live" environment, as this maximizes instantaneous damage, and mobs with DoTs ticking on them (since more will be spawning in constantly).

No surprises with Eco Mode's efficiency. Whether to max Poison Brace or Fire Arrow comes down to a matter of taste. Maxxing Fire Arrow first will give you acceptable DPS, and slightly more efficient mana use, at the cost of losing damage on 4-5 targets. Poison Brace sacrifices mana efficieny and 1-3 target damage in exchange for higher maximum DPS.

I propose a skill point allocation along the lines of:

*Kino's Build*
* 1 pt. -       Teleport        - 30
* MAX -         Fire Arrow      - 31-40
* MAX -         Teleport        - 41-47
* MAX -         Poison Brace    - 47-57
* 3 pts. -      MP Eater        - 57-58
* MAX -         Meditation      - 58-64
* 18 pts. -     Slow            - 65-70

Teleport is your best damage mitigation, so grab that first. Then, max Fire Arrow ASAP to maximize damage. Finish off Teleport, because you are a mage. Max out Poison Brace next, so you can start doing the ABABAB rotation. Limp in to MP Eater, because it is nearly worthless in practice†. Max Meditation (unless you are doing a greed build) to boost group DPS. Finish with Slow, because it is still helpful sometimes (whether Myst benefits from it is still hotly debated).

† With probabilities and % Max MP, MP Eater has a quarter of the mob's max mp to work off of. So for a mob with 150 MP (i.e. Dark/Hybrid Golems), MP Eater has 37.5 MP to eat, equating to +7.5 MP/s. By adjusting the timing of Eco Mode, (i.e. Poison Brace at second zero, and Fire Arrow at second five), it may just barely be MP-postive (with perfect technique). But unless potion economy is a huge deal in Classic World, you are always better off **always casting**. Additionally, you will be kicked very quickly from a party if you sandbag your DPS.

I still wouldn't use or rely on Eco Mode for several reasons:
* You can only use the Eco Mode rotation starting at level 57, which by now, mobs drop 100+ mesos each
* You would still need to stat into MP Eater to be mana-positive (probably c. level 62)
* So, you only get eight "efficient" levels before you gain access to skills that blow this out of the water
* Even still: DPS = Dead mobs = Mesos and junk drops = Potions
* Starting at level 70, mobs have dramatically higher HP, compared to the EXP they give, making DPS the most important consideration
* People will not party with you
* Eco Mode won't apply DoTs to any new mobs that spawn in between casts
