Current simulation flaws
* DoTs are ignored, not reset, if re-applied
* Does not simulate mob respawn/death cycle, which understates effects of DoTs
# Rotation simulation (currently for F/P Mages)
Note: this is not for "MapleStory at home" ;) (not that you'd roll F/P anyway), this is for the upcoming Classic World, with the information we know.

Current simulator results of interest:
| Pattern / Mobs Targeted : DPS | 1           | 2            | 3             | 4            | 5              |   | AVG              | MAX            |
|-------------------------------|-------------|--------------|---------------|--------------|----------------|---|------------------|----------------|
| **BAAA**                      | **59.8375** | **96.97083** | 133.6239583   | **156.7125** | **178.790625** |   | **125.18708266** | **178.790625** |
| BAx4                          | 59.810416   | 94.10625     | 130.897916    | 151.6875     | 175.8125       |   | 122.4629164      | 175.8125       |
| AB                            | 54.82083    | 94.63125     | 133.9416      | 147.8875     | 164.97083      |   | 119.250402       | 164.97083      |
| BAA                           | 56.19583    | 92.125       | 127.55        | 147          | 166.603125     |   | 117.894791       | 166.603125     |
| **Poison Brace (A)**          | 58.90625    | 86.079166    | 114.735416    | 144.825      | 173.464583     |   | 115.602083       | 173.464583     |
| ABBB                          | 49.95       | 92.67083     | **135.20625** | 143.975      | 152.74375      |   | 114.909166       | 152.74375      |
| ABB                           | 50.5427083  | 92.2625      | 132.77083     | 142.8625     | 155.182916     |   | 114.72429086     | 155.182916     |
| ABx4                          | 47.275      | 89.09375     | 130.8802083   | 138.5625     | 145.5916       |   | 110.28061166     | 145.5916       |
| **Fire Arrow (B)**            | 43.13333    | 86.2666      | 130.1         | 131.1        | 130.6          |   | 104.239986       | 131.1          |
| Eco Mode                      | 24.005208   | 43.7666      | 63.5          | 68.325       | 74.234375      |   | 54.7662366       | 74.234375      |

*Figures are in base damage per second (internally called "Potency")*

Special note: "Eco Mode" minimizes casts, and lets the DoTs tick for as long as possible.

I propose a skill point allocation along the lines of:

*Kino's Build*
* 1 pt. -       Teleport        - 30
* MAX -         Poison Brace    - 31-40
* MAX -         Teleport        - 41-47
* MAX -         Fire Arrow      - 47-57
* 3 pts. -      MP Eater        - 57-58
* MAX -         Meditation      - 58-64
* 18 pts. -     Slow            - 65-70

Teleport is your best damage mitigation, so grab that first. Then, max Poison Brace ASAP to maximize damage. Finish off Teleport, because you are a mage. Max out Fire Arrow next, so you can start doing BAAA rotation. Limp in to MP Eater, because it is nearly worthless in practice†. Max Meditation (unless you are doing a greed build) to boost group DPS. Finish with Slow, because it is still helpful sometimes (whether Myst benefits from it is debatable).

† With probabilities and % Max MP, MP Eater has a quarter of the mob's max mp to work off of. So for a mob with 150 MP (i.e. Dark/Hybrid Golems), MP Eater has 37.5 MP to eat, equating to +7.5 MP/s. Unless you are doing some sort of potion Ironman, remember that DPS = Dead mobs = Mesos and junk drops = Potions. Even still, remember that "mana efficiency" goes out the window on the third job advancement.