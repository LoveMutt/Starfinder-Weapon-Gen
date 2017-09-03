import random, sys, time
from random import randint
import string
import argparse, os



damageType = ['Cryo', 'Flame', 'Laser', 'Plasma', 'Projectile', 'Shock', 'Sonic']
damageTypeAbbrv = {'Cryo':' C', 'Flame':' F', 'Laser':' F', 'Plasma':' E & F', 'Projectile':' P', 'Shock':' E', 'Sonic':' So'}
criticalTypeSmall = {'Cryo':['Staggered'], 'Flame':['Burn'], 'Laser':['Burn','Staggered'], 'Plasma':['Burn','Knockdown'], 'Projectile':['Knockdown','-'], 'Shock':['Arc'], 'Sonic':['Knockdown','Deafen']}
criticalTypeLong =  {'Cryo':['Staggered'], 'Flame':['Burn'], 'Laser':['Burn','Staggered','Wound'], 'Plasma':['Burn','Knockdown','Corrode'], 'Projectile':['Knockdown','Wound','-'], 'Shock':['Arc'], 'Sonic':['Knockdown','Deafen']}
criticalTypeHeavy =  {'Cryo':['Staggered','Wound'], 'Flame':['Burn'], 'Laser':['Burn','Staggered','Wound','Severe Wound'], 'Plasma':['Burn','Knockdown','Corrode'], 'Projectile':['Knockdown','Wound','-','Severe Wound'], 'Shock':['Arc'], 'Sonic':['Knockdown','Deafen','Wound']}
criticalTypeSniper =  {'Cryo':['Staggered','Wound'], 'Flame':['Burn','Wound'], 'Laser':['Burn','Staggered','Wound','Severe Wound'], 'Plasma':['Burn','Knockdown','Corrode','Wound'], 'Projectile':['Knockdown','Wound','Severe Wound'], 'Shock':['Arc','Wound'], 'Sonic':['Knockdown','Deafen','Wound']}

armType = ['smallArm', 'Longarm','heavyWeapon', 'sniperWeapon']
special = ['Analog','Automatic','Blast', 'Boost', 'Bright','Entangle','Explode','Injection','Line','Penetrating', 'Quick Reload', 'Sniper', 'Stun', 'Unwieldy']
criticalType = ['Arc', 'Bleed', 'Burn', 'Corrode', 'Deafen', 'Injection DC +2', 'Knockdown', 'Severe wound', 'Staggered', 'Wound']

smallSubType = ['Semi-Auto FX Pistol','FX Machine Pistol','FX Revolver','FX Hand-Cannon']
longSubType = ['FX Rifle','FX Carbine','FX Scattergun','FX Submachine Gun']
heavySubType = ['FX Cannon','Heavy FX Repeater','FX Thrower','FX Railgun']
sniperSubType = ['Shirren-eye FX rifle','Bolt Action FX Rifle','Semi-Auto FX Rifle','Gas-operated FX Rifle']

boostDice = [['1d4','1d6'],['1d6','1d8'],['1d10','1d12'],['2d6','2d8'],['3d6','2d10']]

rangeSmall = [20,30,40]
rangeLong = [30,40,50,60,70]
rangeHeavy = [30,40,50,60,70,80]
rangeSniper = [50,60]

smallArmDamageCurve = {'1':['1d4','1d6'],'2':['1d4','1d6'],'3':['1d6','1d4'],'4':['1d6','1d8'],'5':['1d6','1d8'],'6':['2d4','1d8'],'7':['2d4','2d6'],'8':['2d6','3d4'],'9':['2d6','3d4'],'10':['2d8','3d4'],'11':['2d8','3d6'],'12':['2d8','4d4'],'13':['3d6','4d6'],'14':['5d4','3d8'],'15':['4d6','3d12'],'16':['4d8','3d12'],'17':['8d4','5d8'],'18':['3d12','4d12'],'19':['6d6','4d12'],'20':['5d12','9d6']}

longarmDamageCurve = {'1':['1d6','1d8'],'2':['1d6','1d8'],'3':['1d6','1d8'],'4':['1d8','1d10'],'5':['1d8','1d10'],'6':['1d12','2d6'],'7':['2d6','2d8'],'8':['2d8','2d10'],'9':['3d6','2d10'],'10':['2d10','5d4'],'11':['2d12','3d8'],'12':['2d12','3d10'],'13':['3d10','3d12'],'14':['4d8','4d10'],'15':['4d10','4d12'],'16':['6d8','8d6'],'17':['8d6','12d4'],'18':['7d8','6d10'],'19':['8d8','6d12'],'20':['8d10','12d8']}

heavyDamageCurve = {'1':['1d8','1d10'],'2':['1d10','1d10'],'3':['1d10','1d10'],'4':['1d10','2d6'],'5':['2d6','1d12'],'6':['1d12','2d6'],'7':['2d8','2d6'],'8':['2d8','2d10'],'9':['2d10','2d12'],'10':['2d12','3d8'],'11':['3d8','3d10'],'12':['3d10','4d6'],'13':['4d8','4d10'],'14':['4d12','6d6'],'15':['4d12','6d10'],'16':['5d12','6d10'],'17':['7d8','7d10'],'18':['9d6','8d8'],'19':['8d10','7d12'],'20':['10d10','9d12']}

sniperDamageCurve = {'1':['1d10'],'2':['1d10'],'3':['1d10'],'4':['1d10'],'5':['2d10'],'6':['2d10'],'7':['2d10'],'8':['2d10'],'9':['4d10'],'10':['4d10'],'11':['4d10'],'12':['4d10'],'13':['6d10'],'14':['6d10'],'15':['6d10'],'16':['6d10'],'17':['10d10'],'18':['10d10'],'19':['10d10'],'20':['10d10']}


def smallArm (level):
    
    if int(level) in range(1,5):tier=1
    elif int(level) in range(5,9):tier=2
    elif int(level) in range(9,13):tier=3
    elif int(level) in range(13,17):tier=4
    elif int(level) in range(17,21):tier=5
    
    randDamageType = random.choice(damageType)
    gunType = random.choice(smallSubType)
    printLevel = level
    if gunType == 'FX Hand-Cannon' and level != '20': level = str(int(level)+1)
    damage = random.choice(smallArmDamageCurve[level]) + damageTypeAbbrv[randDamageType]
    
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
        
        
    #AMMO #SPECIAL
    if gunType == 'FX Revolver':
        ammo.append(random.choice(['6 rounds','8 rounds']))
        ammo.append("1")
        special.append(random.choice(['Boost '+ random.choice(boostDice[tier-1]),'Bright','Quick Reload','Stun','-','-']))
    elif gunType == 'FX Hand-Cannon':
        rangeo = 10 + (tier*5) + random.choice([0,5])
        if rangeo > 30: rangeo = 30
        special.append(random.choice(['Blast','Line']))
        special.append('Unwieldy')
        ammo.append('1 shell')
        ammo.append("1")
    elif gunType == 'Semi-Auto FX Pistol':
        semiAuto1= [random.choice(['20','20','40','80']) + ' charges',random.choice(['1','1','2','4'])]
        semiAuto2= [random.choice(['10','12','16','18',]) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        special.append(random.choice(['Boost '+ random.choice(boostDice[tier-1]),'Bright','Quick Reload','Stun','-','-']))
    elif gunType == 'FX Machine Pistol':
        special.append('Automatic')
        semiAuto1= [random.choice(['20','20','40','40']) + ' charges',random.choice(['1','1','2','4'])]
        semiAuto2= [random.choice(['10','12','12','24','48']) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        
    if special == 'Analog, -':special = 'Analog'
        
    #Critical
    critical = (random.choice(criticalTypeSmall[randDamageType]))
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
        
        
    
    print "Level " + printLevel + " " + gunName
    print "Small arm - one-handed"
    print""
    print "Damage:      " + damage
    print "Range:       " + str(rangeo) + " ft."
   
    print "Critical:    " + critical
    
    print "Capacity:    " + ammo[0] 
    print "Usage:       " + ammo[1]
    
    special1 = ', '.join(special)
    if special1.startswith(', '):special1=special1[2:]
    print "Special:     " + special1
    print "Bulk:        L"

def longarm (level):
    
    if int(level) in range(1,5):tier=1
    elif int(level) in range(5,9):tier=2
    elif int(level) in range(9,13):tier=3
    elif int(level) in range(13,17):tier=4
    elif int(level) in range(17,21):tier=5
    
    randDamageType = random.choice(damageType)
    gunType = random.choice(longSubType)
    printLevel = level
    if gunType == 'FX Rifle' and level != '20': level = str(int(level)+1)
    damage = random.choice(longarmDamageCurve[level]) + damageTypeAbbrv[randDamageType]
    
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
        semiAuto1= [random.choice(['20','40','80','100']) + ' charges',random.choice(['1','2','4','10'])]
        semiAuto2= [random.choice(['6','12','18']) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        special.append(random.choice(['Boost '+ random.choice(boostDice[tier-1]),'Penetrating','Quick Reload','-']))
        Bulk = random.choice(['1','1','2'])
    elif gunType == 'FX Carbine':
        semiAuto1= [random.choice(['60','80','100']) + ' charges',random.choice(['1','2','4','10'])]
        semiAuto2= [random.choice(['12','24','48',]) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        special.append(random.choice(['Automatic','Boost '+ random.choice(boostDice[tier-1]),'Stun','-']))
        rangeo = rangeo - 30
        if rangeo < 40: rangeo = 40
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
    critical = (random.choice(criticalTypeLong[randDamageType]))
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
        
        
    
    print "Level " + printLevel + " " + gunName
    print "Longarm - two-handed"
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

def heavy (level):

    if int(level) in range(1,5):tier=1
    elif int(level) in range(5,9):tier=2
    elif int(level) in range(9,13):tier=3
    elif int(level) in range(13,17):tier=4
    elif int(level) in range(17,21):tier=5
    
    randDamageType = random.choice(damageType)
    gunType = random.choice(heavySubType)
    printLevel = level
    if gunType == 'FX Railgun' and level != '20': level = str(int(level)+1)
    damage = random.choice(heavyDamageCurve[level]) + damageTypeAbbrv[randDamageType]
    
    gunName = gunType.replace('FX',randDamageType)
    
    special = []
    ammo = []
    #Range
    rangeo = 0
    rangeo=random.choice(rangeHeavy)
    rangeo=rangeo+(10*tier)
    if randDamageType == 'Laser':
            rangeo = rangeo + 30
    if rangeo > 120: rangeo = 120
    
    special.append(random.choice(['Analog','','','']))
        
    if gunType == 'FX Cannon':
        gunName = gunName.replace("Projectile ","")
        ammo= [random.choice(['40','80','100']) + ' charges',random.choice(['2','4','5','10'])]
        rad =  5*tier
        rangeo = rangeo - 30
        if rangeo < 30: rangeo = 30
        special.append('Explode ('+str(rad)+' ft.)')
        special.append('Unwieldy')
        
    elif gunType == 'Heavy FX Repeater':
        gunName = gunName.replace("Projectile ","")
        semiAuto1= [random.choice(['60','80','100']) + ' charges',random.choice(['1','2','4','10'])]
        semiAuto2= [random.choice(['12','24','48',]) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        special.append('Automatic')
        special.append(random.choice(['Penetrating','']))
        rangeo = rangeo - 30
        
    elif gunType == 'FX Thrower':
        gunName = gunName.replace("Projectile","Laser")
        special.append(random.choice(['Blast','Line']))
        special.append('Unwieldy')
        rangeo = 10 + (tier*5) + random.choice([0,5])
        if rangeo > 30: rangeo = 30
        ammo = [random.choice(['60','80','100']) + ' charges',random.choice(['2','4','10'])]
        
    elif gunType == 'FX Railgun':
        gunName = gunName.replace("Projectile ","")
        special.append('Line')
        special.append('Penetrating')
        special.append('Unwieldy')
        semiAuto1= [random.choice(['20','40']) + ' charges',random.choice(['2','4','10'])]
        semiAuto2= [random.choice(['8','12','18','24']) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        
    Bulk = random.choice(['2','2','3'])    
    if special == 'Analog, -':special = 'Analog'
        
    #Critical
    critical = (random.choice(criticalTypeHeavy[randDamageType]))
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
        
    print "Level " + printLevel + " " + gunName
    print "Heavy - two-handed"
    print ""
    
    print "Damage:      " + damage
    print "Range:       " + str(rangeo) + " ft."
   
    print "Critical:    " + critical
    
    print "Capacity:    " + ammo[0] 
    print "Usage:       " + ammo[1]
    
    special1 = ', '.join(special)
    if special1.startswith(', '):special1=special1[2:]
    if special1.endswith(', '):special1=special1[:-2]
    print "Special:     " + special1
    print "Bulk:        " + Bulk
   
def sniper (level):

    if int(level) in range(1,5):tier=1
    elif int(level) in range(5,9):tier=2
    elif int(level) in range(9,13):tier=3
    elif int(level) in range(13,17):tier=4
    elif int(level) in range(17,21):tier=5
    
    randDamageType = random.choice(damageType)
    gunType = random.choice(sniperSubType)
    printLevel = level
    if gunType == 'Shirren-eye FX Rifle' and level != '20': level = str(int(level)+1)
    damage = random.choice(sniperDamageCurve[level]) + damageTypeAbbrv[randDamageType]
    
    gunName = gunType.replace('FX',randDamageType)
    
    special = []
    ammo = []
    #Range
    rangeo = 0
    rangeo=random.choice(rangeSniper)
    rangeo=rangeo+(10*tier)
    if randDamageType == 'Laser' or randDamageType == 'Projectile':
            rangeo = rangeo + 20
    if rangeo > 100: rangeo = 100
    
    
    if randDamageType == "Projectile":
        special.append(random.choice(['Analog','']))
       
    gunName = gunName.replace("Projectile ","")  
    
    if gunType == 'Shirren-eye FX rifle':
        ammo= [random.choice(['4','6','8',]) + ' rounds','1']

    elif gunType == 'Bolt Action FX Rifle':
        ammo= ['1 round','1']
        
    elif gunType == 'Semi-Auto FX Rifle':
        semiAuto1= [random.choice(['20','40','60','80']) + ' charges',random.choice(['5','10','20'])]
        semiAuto2= [random.choice(['4','8','12','16']) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
        
    elif gunType == 'Gas-operated FX Rifle':
        semiAuto1= [random.choice(['20','40']) + ' charges',random.choice(['2','4','10'])]
        semiAuto2= [random.choice(['4','8','12',]) + ' rounds','1']
        ammo=random.choice([semiAuto1,semiAuto2])
    
    #add sniper range    
    rad =  250*tier
    if rad > 1000: rad = 1000
    special.append(random.choice(['Bright','Penetrating','']))
    special.append('Sniper ('+str(rad)+' ft.)')
    special.append('Unwieldy')
    
        
    Bulk = random.choice(['1','2'])    
    if special == 'Analog, -':special = 'Analog'
        
    #Critical
    critical = (random.choice(criticalTypeSniper[randDamageType]))
    if tier in [1,2]: critical = random.choice([critical,'-'])#possibilty of no critical in low tiers
    
    if critical in ['Burn','Arc','Corrode']:
        if int(level) in range(1,9):
            num=1
            die=random.choice(['4','6'])
        elif int(level) in range(9,14):
            num=2
            die=random.choice(['4','6','8'])
        elif int(level) in range(14,19):
            num=3
            die=random.choice(['4','6','8'])
        elif int(level) in range(19,21):
            num=4
            die=random.choice(['4','6','8'])
        else: print level + 'wrong'
        critical = critical + ' ' + str(num) +'d' + str(die)
        
    print "Level " + printLevel + " " + gunName
    print "Sniper - two-handed"
    print ""
    
    print "Damage:      " + damage
    print "Range:       " + str(rangeo) + " ft."
   
    print "Critical:    " + critical
    
    print "Capacity:    " + ammo[0] 
    print "Usage:       " + ammo[1]
    
    special1 = ', '.join(special)
    if special1.startswith(', '):special1=special1[2:]
    if special1.endswith(', '):special1=special1[:-2]
    print "Special:     " + special1
    print "Bulk:        " + Bulk
    
def main():
    
    #argument parser
    parser=argparse.ArgumentParser(prog = 'WeaponGen.py',description = 'Starfinder random weapon generator')
    parser.add_argument('-a','--armtype',choices=set(('smallarm', 'longarm', 'heavy', 'sniper')),dest='type', help = 'choose type of weapon')
    levels = parser.add_mutually_exclusive_group()
    levels.add_argument('-t','--tier', type=int, choices=set((1, 2, 3, 4, 5)),dest='tier', help='choose weapon tier, tier 1 is levels 1-4, 2 is 5-8, etc.')
    levels.add_argument('-l','--level', type=int, choices=set(range(1, 21)),dest='level', help='choose weapon level 1-20')

    global results    
    results =  parser.parse_args()
    
    tier = results.tier
    type = results.type
    level= results.level
    
    print ""
    spin="\|/-\|/-"
    for l in spin:
        sys.stdout.write(l)
        sys.stdout.flush()
        sys.stdout.write('\b')
        time.sleep(0.1)
    
    if level is not None:
        levelA = str(level)
    elif level is None:    
        if tier is None:
            levelA = str(randint(1,20))
        elif tier == 1:levelA = str(randint(1,4))
        elif tier == 2:levelA = str(randint(5,8))
        elif tier == 3:levelA = str(randint(9,12))
        elif tier == 4:levelA = str(randint(13,16))
        elif tier == 5:levelA = str(randint(17,20))
    
    if type is None: arm = random.choice([1,2,3,4])
    elif type == 'smallarm': arm = 1
    elif type == 'longarm': arm =2
    elif type == 'heavy': arm = 3
    elif type == 'sniper':arm = 4
    
    if arm == 1: smallArm(levelA)
    if arm == 2: longarm(levelA)
    if arm == 3: heavy(levelA)
    if arm == 4: sniper(levelA)
        
if __name__ == "__main__":
    main()    
     