# Starfinder-Weapon-Gen
This script will generate a randomised small arm, longarm, or heavy weapon with damage curves matched as closely as possible to the core rulebook weapon entries.

It's dirty and I'm not ashamed. But it works quite well and can add some add some fun items to your game while keeping it balanced.

### Usage: 

	WeaponGen.py [OPTIONS]
	optional arguments:
		-h,--help				show help
		-t,--tier {1,2,3,4,5}			choose weapon tier. 1,2,3,4,5 corresponds to levels 1-4,5-8,9-12,13-16,17-20
		-a,--armtype {heavy,smallarm,longarm}	choose weapon type

	
if you run WeaponGen.py with no arguments it will create a completely random weapon from any type or tier.
example use cases:

I want to generate some loot for a level 2 party. I would run [ WeaponGen.py -t 1 ] to generate a level 1-4 weapon of a random type.

My shop wants a new longarm for a level 14 character. I would run [ WeaponGen.py -t 4 -a longarm ] to get a longarm in the right tier

### Example outputs:

	Level 4 Laser Revolver

	Damage:      1d6 F
	Range:       50 ft.
	Critical:    Burn 1d6
	Capacity:    6 rounds
	Usage:       1
	Special:     Stun
	Bulk:        L
	
	Level 5 Sonic Machine Pistol

	Damage:      1d6 So
	Range:       50 ft.
	Critical:    Deafen
	Capacity:    48 rounds
	Usage:       1
	Special:     Automatic
	Bulk:        L
	
	Level 12 Plasma Rifle

	Damage:      3d10 E & F
	Range:       100 ft.
	Critical:    Burn 2d8
	Capacity:    80 charges
	Usage:       4
	Special:     Analog
	Bulk:        2

	Level 13 Cryo Scattergun

	Damage:      3d10 C
	Range:       30 ft.
	Critical:    Staggered
	Capacity:    12 shells
	Usage:       1
	Special:     Blast
	Bulk:        1
	
	Level 7 Shock Railgun

	Damage:      2d8 E
	Range:       60 ft.
	Critical:    Arc 1d4
	Capacity:    24 rounds
	Usage:       1
	Special:     Line, Penetrating, Unwieldy
	Bulk:        2

