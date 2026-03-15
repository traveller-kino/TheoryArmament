# YAMETE KUDASTOOOOOP! These numbers are obsolete, as I need to re-run the sims
# Rotation simulation (currently for F/P Mages)
Note: this is not for "MapleStory at home" ;) (not that you'd roll F/P anyway), this is for the upcoming Classic World, with the information we know.


Current simulator results of interest:
| Pattern / Mobs Targeted : DPS 	| 1         	| 2          	| 3          	| 4       	| 5         	|   	| AVG         	| MAX       	|
|-------------------------------	|-----------	|------------	|------------	|---------	|-----------	|---	|-------------	|-----------	|
| **ABABAB**                    	| 27.441666 	| 48.1979166 	| 68.9635416 	| 75.8875 	| 78.575    	|   	| 59.81312484 	| 78.575    	|
| ABBB                          	| 25.0875   	| 47.364583  	| 69.3802083 	| 74.2    	| 76.028125 	|   	| 58.41208326 	| 76.028125 	|
| BAA                           	| 26.690625 	| 45.1       	| 62.76666   	| 72      	| 73.603125 	|   	| 56.032082   	| 73.603125 	|
| BAAA                          	| 27.0135   	| 44.1604    	| 60.73958   	| 71.75   	| 73.634375 	|   	| 55.459571   	| 73.634375 	|
| ABx4                          	| 23.4      	| 44.5333    	| 65.4666    	| 68.7    	| 70.9      	|   	| 54.59998    	| 70.9      	|
| ABB                           	| 23.554166 	| 42.79375   	| 62.675     	| 67.7625 	| 69.075    	|   	| 53.1720832  	| 69.075    	|
| **Fire Arrow (B)**            	| 21.433333 	| 42.866666  	| 64.3       	| 63.7    	| 64.4      	|   	| 51.3399998  	| 64.4      	|
| **Poison Brace (A)**          	| 26.625    	| 39.627083  	| 53.446875  	| 66.8625 	| 67.9875   	|   	| 50.9097916  	| 67.9875   	|
| **Eco Mode**                  	| 15.58333  	| 27.6333    	| 40.64125   	| 45.75   	| 47.690625 	|   	| 35.459701   	| 47.690625 	|

*Figures are in base damage per second (internally called "Potency")*

Special note: "Eco Mode" is casting Poison Brace & Fire Arrow, and waiting for the poison DoT to expire. While it isn't particularly good, it's interesting knowing it's only c. 40% less than other rotations.

Alternating Poison Brace & Fire Arrow results in the highest DPS. This makes sense, especially in a "live" environment, as this maximizes instantaneous damage, and mobs with DoTs ticking on them (since more will be spawning in constantly).

| Pattern / Efficiency Metric | AVG MP/S | DMG/MP           |
|-----------------------------|----------|------------------|
| **Eco Mode**                | 6.363636 | 5.57223904698509 |
| ABBB                        | 10.8333  | 5.39190119908061 |
| **Fire Arrow (B)**          | 10       | 5.13399998       |
| **ABABAB**                  | 11.6666  | 5.12686856839182 |
| ABx4                        | 10.6666  | 5.11878011737573 |
| ABB                         | 11.1111  | 4.78549227349227 |
| BAA                         | 12.2222  | 4.58445140809347 |
| BAAA                        | 12.5     | 4.43676568       |
| **Poison Brace (A)**        | 13.3333  | 3.81824391560979 |

No surprises with Eco Mode. Fire Arrow only comes just ahead of the highest DPS pattern, so this is good indication that dual F/P mages in Classic World should **max Fire Arrow first**, because the DPS is better than Poison Brace only, and is more MP efficient. 

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

† With probabilities and % Max MP, MP Eater has a quarter of the mob's max mp to work off of. So for a mob with 150 MP (i.e. Dark/Hybrid Golems), MP Eater has 37.5 MP to eat, equating to +7.5 MP/s. By adjusting the timing of Eco Mode, (i.e. Poison Brace at second zero, and Fire Arrow at second five), it may just barely be MP-postive (with perfect technique). But unless potion economy is a huge deal in Classic World, you are always better off **always casting**. Additionally, you will be kicked very quickly from a party if you limp your DPS.

I still wouldn't use or rely on Eco Mode for several reasons:
* You can only use the Eco Mode rotation starting at level 57, which by now, mobs drop 100+ mesos each
* You would still need to stat into MP Eater to be mana-positive (probably c. level 62)
* So, you only get eight "efficient" levels before you gain access to skills that blow this out of the water
* Even still: DPS = Dead mobs = Mesos and junk drops = Potions
* Starting at level 70, mobs have dramatically higher HP, compared to the EXP they give, making DPS the most important consideration
* People will not party with you
* Eco Mode won't apply DoTs to any new mobs that spawn in between casts

However, this does lead to an idea of a forbidden MP-neutral build... So, in theory:

(Assumptions: Max MP will be c. 2000-3000)

*Eureka Build*

First Job Advancement
* 1 pt.     -       Energy Bolt             - 10
* 15 pts.   -       Magic Claw              - 11-15
* MAX       -       Magic Guard             - 16-20
* MAX       -       Improved MP Recovery    - 21-25
* MAX       -       MAX MP Increase         - 26-30

Important effects
* Improved MP Recovery: yields +2-3.00 MP/s

Second Job Advancement
* 1 pt.     -   Teleport        - 30
* MAX       -   Fire Arrow      - 31-40
* MAX       -   Teleport        - 41-47
* MAX       -   Poison Brace    - 47-57
* MAX       -   MP Eater        - 57-63
* MAX       -   Meditation      - 64-70

Important effects
* MP Eater: yields +9 MP/s (boosted by Improved MP Recovery, base +7.5 MP/s)

With a target of 11.666 MP/s, this build would reach c. -0.666 to 0.334 MP/s

As a frame of reference:

The base MP/s equates to one Mana Elixir every 25.71 seconds

The bottom band equates to one Mana Elixir every 7.5 minutes

The top band will never need potions

In mesos (620/elixir):

Base MP/s:          24.11 mesos/second

Bottom band MP/s:   1.37 mesos/second

Top band MP/s:      0.00 mesos/second

If Improved MP Recovery does not boost MP Eater:

Base MP/s: 24.11 mesos/second

Bottom band MP/s: 4.49 mesos/second

Top band MP/s: 2.40 mesos/second