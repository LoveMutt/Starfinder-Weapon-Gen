import random, sys, time
from random import randint
import string
import argparse, os



damageType = ['Cryo', 'Flame', 'Laser', 'Plasma', 'Projectile', 'Shock', 'Sonic']
damageTypeAbbrv = {'Cryo':' C', 'Flame':' F', 'Laser':' F', 'Plasma':' E & F', 'Projectile':' P', 'Shock':' E', 'Sonic':' So'}
damageTypeSmall = {'Cryo':['Staggered'], 'Flame':['Burn'], 'Laser':['Burn','Staggered'], 'Plasma':['Burn','Knockdown'], 'Projectile':['Knockdown','-'], 'Shock':['Arc'], 'Sonic':['Knockdown','Deafen']}
damageTypeLong =  {'Cryo':['Staggered'], 'Flame':['Burn'], 'Laser':['Burn','Staggered','Wound'], 'Plasma':['Burn','Knockdown','Corrode'], 'Projectile':['Knockdown','Wound','-'], 'Shock':['Arc'], 'Sonic':['Knockdown','Deafen']}
damageTypeLong =  {'Cryo':['Staggered','Wound'], 'Flame':['Burn'], 'Laser':['Burn','Staggered','Wound','Severe Wound'], 'Plasma':['Burn','Knockdown','Corrode'], 'Projectile':['Knockdown','Wound','-','Severe Wound'], 'Shock':['Arc'], 'Sonic':['Knockdown','Deafen','Wound']}

p = ['Arc', 'Bleed', 'Burn', 'Corrode', 'Deafen', 'Injection DC +2', 'Knockdown', 'Severe wound', 'Staggered', 'Wound']



armType = ['smallArm', 'Longarm','heavyWeapon', 'sniperWeapon']

special = ['Analog','Automatic','Blast', 'Boost', 'Bright','Entangle','Explode','Injection','Line','Penetrating', 'Quick Reload', 'Sniper', 'Stun', 'Unwieldy']

criticalType = ['Arc', 'Bleed', 'Burn', 'Corrode', 'Deafen', 'Injection DC +2', 'Knockdown', 'Severe wound', 'Staggered', 'Wound']

subType = ['FX Pistol','Semi-Auto FX Pistol','FX Revolver','FX Hand-Cannon']
longSubType = ['FX Rifle','FX Carbine','FX Scattergun','FX Submachine Gun']
heavySubType = ['FX Cannon','FX Machine Gun','FX Thrower','FX Railgun']

boostDice = [['1d4','1d6'],['1d6','1d8'],['1d10','1d12'],['2d6','2d8'],['3d6','2d10']]

rangeSmall = [20,30,40]
rangeLong = [30,40,50,60,70]
rangeHeavy = [30,40,50,60,70]

smallArmDamage = {'1':['1d4','1d6'],'2':['1d4','1d6'],'3':['1d6','1d4'],'4':['1d6','1d8'],'5':['1d6','1d8'],'6':['2d4','1d8'],'7':['2d4','2d6'],'8':['2d6','3d4'],'9':['2d6','3d4'],'10':['2d8','3d4'],'11':['2d8','3d6'],'12':['2d8','4d4'],'13':['3d6','4d6'],'14':['5d4','3d8'],'15':['4d6','3d12'],'16':['4d8','3d12'],'17':['8d4','5d8'],'18':['3d12','4d12'],'19':['6d6','4d12'],'20':['5d12','9d6']}

longarmDamage = {'1':['1d6','1d8'],'2':['1d6','1d8'],'3':['1d6','1d8'],'4':['1d8','1d10'],'5':['1d8','1d10'],'6':['1d12','2d6'],'7':['2d6','2d8'],'8':['2d8','2d10'],'9':['3d6','2d10'],'10':['2d10','5d4'],'11':['2d12','3d8'],'12':['2d12','3d10'],'13':['3d10','3d12'],'14':['4d8','4d10'],'15':['4d10','4d12'],'16':['6d8','8d6'],'17':['8d6','12d4'],'18':['7d8','6d10'],'19':['8d8','6d12'],'20':['8d10','12d8']}

heavyDamage = '1':['1d8','1d10'],'2':['1d10','1d10'],'3':['1d10','1d10'],'4':['1d10','2d6'],'5':['2d6','1d12'],'6':['1d12','2d6'],'7':['2d8','2d6'],'8':['2d8','2d10'],'9':['2d10','2d12'],'10':['2d12','3d8'],'11':['3d8','3d10'],'12':['3d10','4d6'],'13':['4d8','4d10'],'14':['4d12','6d6'],'15':['4d12','6d10'],'16':['5d12','6d10'],'17':['7d8','7d10'],'18':['9d6','8d8'],'19':['8d10','7d12'],'20':['10d10','9d12'],

def smallArm ():
    level = str(randint(1,20))
    
    if int(level) in range(1,5):tier=1
    elif int(level) in range(5,9):tier=2
    elif int(level) in range(9,13):tier=3
    elif int(level) in range(13,17):tier=4
    elif int(level) in range(17,21):tier=5
    
    
    
    randDamageType = random.choice(damageType)
    gunType = random.choice(subType)
    damage = random.choice(smallArmDamage[level]) + damageTypeAbbrv[randDamageType]
    
    gunName = gunType.replace('FX',randDamageType).replace("Projectile ","")
    
    special = []
    ammo = []
    #Range
    rangeo = 0
    rangeo=random.choice(rangeSmall)
    rangeo=rangeo+(10*tier)
    if tier == 5:
            rangeo = rangeo - 10
    if randDamageType == 'Laser':
            rangeo = rangeo + 20
    if rangeo > 100: rangeo = 100
    
    #SPECIAL
    special.append(random.choice(['Analog','','']))
    if gunType == 'FX Hand-Cannon':
        rangeo = 10 + (tier*5) + random.choice([0,5])
        if rangeo > 30: rangeo = 30
        special.append(random.choice(['Blast','Line']))
        special.append('Unwieldy')

    elif gunType == 'Semi-Auto FX Pistol':

        special.append('Automatic')
    else:
        special.append(random.choice(['Boost '+ random.choice(boostDice[tier-1]),'Bright','Quick Reload','Stun','-','-']))
        
    #AMMO
    if gunType == 'FX Revolver':
        ammo.append(random.choice(['6 rounds','8 rounds']))
        ammo.append("1")
    elif gunType == 'FX Hand-Cannon':
        ammo.append('1 shell')
        ammo.append("1")
    elif gunType == 'FX Pistol':
        semiAuto1= [random.choice(['20','20','40','80']) + ' charges',random.choice(['1','1','2','4'])]
        semiAuto2= [random.choice(['10','12','16','18',]) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
    elif gunType == 'Semi-Auto FX Pistol':
        semiAuto1= [random.choice(['20','20','40','40']) + ' charges',random.choice(['1','1','2','4'])]
        semiAuto2= [random.choice(['10','12','12','24','48']) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        
    if special == 'Analog, -':special = 'Analog'
        
    #Critical
    critical = (random.choice(damageTypeSmall[randDamageType]))
    if tier in [1,2]: critical = random.choice([critical,critical,'-'])#possibilty of no critical in low tiers
    
    if critical in ['Burn','Arc']:
        if int(level) in range(1,12):
            num=1
            die=random.choice(['4','6'])
        elif int(level) in range(12,16):
            num=2
            die=random.choice(['4','6','8'])
        elif int(level) in range(16,19):
            num=3
            die=random.choice(['4','6','8'])
        elif int(level) in range(19,21):
            num=4
            die=random.choice(['4','6','8'])
        else: print level + 'wrong'
        critical = critical + ' ' + str(num) +'d' + str(die)
        
        
    
    print "Level " + level + " " + gunName
    print ""

    print "Damage:      " + damage
    print "Range:       " + str(rangeo) + " ft."
   
    print "Critical:    " + critical
    
    print "Capacity:    " + ammo[0] 
    print "Usage:       " + ammo[1]
    
    special1 = ', '.join(special)
    if special1.startswith(', '):special1=special1[2:]
    print "Special:     " + special1
    print "Bulk:        L"

def longarm ():
    level = str(randint(1,20))
    
    if int(level) in range(1,5):tier=1
    elif int(level) in range(5,9):tier=2
    elif int(level) in range(9,13):tier=3
    elif int(level) in range(13,17):tier=4
    elif int(level) in range(17,21):tier=5
    
    
    
    randDamageType = random.choice(damageType)
    gunType = random.choice(longSubType)
    if gunType == 'FX Rifle' and level != '20': level = str(int(level)+1)
    damage = random.choice(longarmDamage[level]) + damageTypeAbbrv[randDamageType]
    
    gunName = gunType.replace('FX',randDamageType).replace("Projectile ","")
    
    special = []
    ammo = []
    #Range
    rangeo = 0
    rangeo=random.choice(rangeLong)
    rangeo=rangeo+(10*tier)
    if randDamageType == 'Laser':
            rangeo = rangeo + 20
    if rangeo > 120: rangeo = 120
    
    #SPECIAL
    special.append(random.choice(['Analog','','']))
        
    #AMMO
    if gunType == 'FX Rifle':
        semiAuto1= [random.choice(['20','40','80','100']) + ' charges',random.choice(['1','2','4'])]
        semiAuto2= [random.choice(['6','12','18','24',]) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        special.append(random.choice(['Boost '+ random.choice(boostDice[tier-1]),'Penetrating','Quick Reload','-']))
        Bulk = random.choice(['1','1','2'])
    elif gunType == 'FX Carbine':
        semiAuto1= [random.choice(['60','80','100']) + ' charges',random.choice(['1','2','4','10'])]
        semiAuto2= [random.choice(['12','24','48',]) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        special.append(random.choice(['Automatic','Boost '+ random.choice(boostDice[tier-1]),'Stun','-']))
        rangeo = rangeo - 30
        Bulk = 'L'
    elif gunType == 'FX Scattergun':
        special.append('Blast')
        rangeo = 10 + (tier*5) + random.choice([0,5])
        if rangeo > 30: rangeo = 30
        ammo.append(random.choice(['1 shell','2 shells','6 shells','12 shells']))
        ammo.append("1")
        Bulk = '1'
    elif gunType == 'FX Submachine Gun':
        special.append('Automatic')
        semiAuto1= [random.choice(['20','40']) + ' charges',random.choice(['1','1','2','4'])]
        semiAuto2= [random.choice(['10','12','12','24','48']) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        Bulk = random.choice(['1','1','2'])
        
    if special == 'Analog, -':special = 'Analog'
        
    #Critical
    critical = (random.choice(damageTypeLong[randDamageType]))
    if tier in [1,2]: critical = random.choice([critical,critical,'-'])#possibilty of no critical in low tiers
    
    if critical in ['Burn','Arc','Corrode']:
        if int(level) in range(1,12):
            num=1
            die=random.choice(['4','6'])
        elif int(level) in range(12,16):
            num=2
            die=random.choice(['4','6','8'])
        elif int(level) in range(16,19):
            num=3
            die=random.choice(['4','6','8'])
        elif int(level) in range(19,21):
            num=4
            die=random.choice(['4','6','8'])
        else: print level + 'wrong'
        critical = critical + ' ' + str(num) +'d' + str(die)
        
        
    
    print "Level " + level + " " + gunName
    print ""

    print "Damage:      " + damage
    print "Range:       " + str(rangeo) + " ft."
   
    print "Critical:    " + critical
    
    print "Capacity:    " + ammo[0] 
    print "Usage:       " + ammo[1]
    
    special1 = ', '.join(special)
    if special1.startswith(', '):special1=special1[2:]
    print "Special:     " + special1
    print "Bulk:        " + Bulk

def heavy ():
    level = str(randint(1,20))
    
    if int(level) in range(1,5):tier=1
    elif int(level) in range(5,9):tier=2
    elif int(level) in range(9,13):tier=3
    elif int(level) in range(13,17):tier=4
    elif int(level) in range(17,21):tier=5
    
    
    
    randDamageType = random.choice(damageType)
    gunType = random.choice(heavySubType)
    if gunType == 'FX Railgun' and level != '20': level = str(int(level)+2)
    damage = random.choice(heavyDamage[level]) + damageTypeAbbrv[randDamageType]
    
    gunName = gunType.replace('FX',randDamageType).replace("Projectile ","")
    
    special = []
    ammo = []
    #Range
    rangeo = 0
    rangeo=random.choice(rangeHeavy)
    rangeo=rangeo+(10*tier)
    if randDamageType == 'Laser':
            rangeo = rangeo + 30
    if rangeo > 120: rangeo = 120
    
    #SPECIAL
    special.append(random.choice(['Analog','','']))
        
    #AMMO
    if gunType == 'FX Cannon':
        ammo= [random.choice(['40','80','100']) + ' charges',random.choice(['2','4','5','10'])]
        rad =  5*tier
        if rangeo > 20: rangeo = 20
        special.append('Explode ('+rad+' ft.)','Unwieldy')
        Bulk = random.choice(['1','1','2'])
    elif gunType == 'FX Machine Gun':
        semiAuto1= [random.choice(['60','80','100']) + ' charges',random.choice(['1','2','4','10'])]
        semiAuto2= [random.choice(['12','24','48',]) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        special.append('Automatic')
        rangeo = rangeo - 30
        Bulk = 'L'
    elif gunType == 'FX Thrower':
        special.append(random.choice(['Blast','Line']))
        rangeo = 10 + (tier*5) + random.choice([0,5])
        if rangeo > 30: rangeo = 30
        ammo.append(random.choice(['1 shell','2 shells','6 shells','12 shells']))
        ammo.append("1")
        Bulk = '1'
    elif gunType == 'FX Railgun':
        special.append('Automatic')
        semiAuto1= [random.choice(['20','40']) + ' charges',random.choice(['1','1','2','4'])]
        semiAuto2= [random.choice(['10','12','12','24','48']) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        Bulk = random.choice(['1','1','2'])
        
    if special == 'Analog, -':special = 'Analog'
        
    #Critical
    critical = (random.choice(damageTypeLong[randDamageType]))
    if tier in [1,2]: critical = random.choice([critical,critical,'-'])#possibilty of no critical in low tiers
    
    if critical in ['Burn','Arc','Corrode']:
        if int(level) in range(1,12):
            num=1
            die=random.choice(['4','6'])
        elif int(level) in range(12,16):
            num=2
            die=random.choice(['4','6','8'])
        elif int(level) in range(16,19):
            num=3
            die=random.choice(['4','6','8'])
        elif int(level) in range(19,21):
            num=4
            die=random.choice(['4','6','8'])
        else: print level + 'wrong'
        critical = critical + ' ' + str(num) +'d' + str(die)
        
        
    
    print "Level " + level + " " + gunName
    print ""

    print "Damage:      " + damage
    print "Range:       " + str(rangeo) + " ft."
   
    print "Critical:    " + critical
    
    print "Capacity:    " + ammo[0] 
    print "Usage:       " + ammo[1]
    
    special1 = ', '.join(special)
    if special1.startswith(', '):special1=special1[2:]
    print "Special:     " + special1
    print "Bulk:        " + Bulk
    
    
def main():
    
    print ""
    blah="\|/-\|/-"
    for l in blah:
        sys.stdout.write(l)
        sys.stdout.flush()
        sys.stdout.write('\b')
        time.sleep(0.1)
    
    longarm()
        
        
        
if __name__ == "__main__":
    main()    
     