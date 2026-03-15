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

Special note: "eco mode" is casting Poison Brace & Fire Arrow, and waiting for the poison DoT to expire. While it isn't particularly good, it's interesting knowing it's only c. 40% less than other rotations.

Alternating Poison Brace & Fire Arrow results in the highest DPS. This makes sense, especially in a "live" environment, as this maximizes instantaneous damage, and mobs with DoTs ticking on them (since more will be spawning in constantly).