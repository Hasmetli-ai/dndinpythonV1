import random
import time
from math import floor
from Enemys import enemy_hp
ac=0
monster_exp=0
enemy_choose=0
choose=None
new_stats=[]
available=[15, 14, 13, 12, 10, 8]
stats={"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
stat_names=["strength","dexterity","constitution","wisdom","intelligence","charisma"]
dex_modifier=0
str_modifier=0
con_modifier=0
cha_modifier=0
int_modifier=0
wis_modifier=0
arrow=0
level=0
exp=0
inventory=[]
total_gp=0
own_class=None
exp=0
your_ac=0
level_exp_requirements = {
    1: 0,
    2: 300,
    3: 900,
    4: 2700,
    5: 6500,
    6: 14000,
    7: 23000,
    8: 34000,
    9: 48000,
    10: 64000,
    11: 85000,
    12: 100000,
    13: 120000,
    14: 140000,
    15: 165000,
    16: 195000,
    17: 225000,
    18: 265000,
    19: 305000,
    20: 355000
}
        
        
        
def class_pick_session():
    all_classes=["Druid","Warrior","Barbarian","Rogue","Bard","Cleric"
                 ,"Monk","Paladin","Ranger","Sorcerer","Wizard","Warlock"]
    global own_class
    print("First of all lets select your class!! TwT\n There have so much enjoyable class !! pick one of them information !!")
    time.sleep(1)
    print(all_classes)
    while True:
        info_class = input("\nWhich class do you want to learn about? (type 'exit' to stop): ").lower()
        if info_class == "exit":
            break
        elif info_class == "barbarian":
            print("Barbarian: a fierce warrior who fights in a rage, taking less damage and hitting harder. Hit die: d12.")
            time.sleep(2)
            print("Main stats: Strength (damage), Constitution (health)")
        elif info_class == "bard":
            print("Bard: a charismatic performer who inspires allies and casts spells with music. Hit die: d8.")
            time.sleep(2)
            print("Main stats: Charisma (spells), Dexterity")
        elif info_class == "cleric":
            print("Cleric: a holy caster who heals allies and channels divine power. Hit die: d8.")
            time.sleep(2)
            print("Main stats: Wisdom (spells), Constitution")
        elif info_class == "druid":
            print("Druid: a nature caster who can shapeshift into animals. Hit die: d8.")
            time.sleep(2)
            print("Main stats: Wisdom (spells), Constitution")
        elif info_class == "warrior":
            print("Warrior : a master of weapons and armor with many attacks. Hit die: d10.")
            time.sleep(2)
            print("Main stats: Strength or Dexterity, Constitution")
        elif info_class == "monk":
            print("Monk: a martial artist who fights unarmed with speed and ki. Hit die: d8.")
            time.sleep(2)
            print("Main stats: Dexterity, Wisdom")
        elif info_class == "paladin":
            print("Paladin: a holy knight bound by an oath, strong in melee with healing and smites. Hit die: d10.")
            time.sleep(2)
            print("Main stats: Strength, Charisma")
        elif info_class == "ranger":
            print("Ranger: a wilderness hunter good with bows, tracking and survival. Hit die: d10.")
            time.sleep(2)
            print("Main stats: Dexterity, Wisdom")
        elif info_class == "rogue":
            print("Rogue: a sneaky expert in stealth, skills and Sneak Attack damage. Hit die: d8.")
            time.sleep(2)
            print("Main stats: Dexterity")
        elif info_class == "sorcerer":
            print("Sorcerer: a caster born with innate magic who can twist spells with metamagic. Hit die: d6.")
            time.sleep(2)
            print("Main stats: Charisma, Constitution")
        elif info_class == "warlock":
            print("Warlock: a caster who gets power from a pact with a patron. Hit die: d8.")
            time.sleep(2)
            print("Main stats: Charisma, Constitution")
        elif info_class == "wizard":
            print("Wizard: a scholar who learns many spells from spellbooks. Hit die: d6.")
            time.sleep(2)
            print("Main stats: Intelligence, Dexterity")
        else:
            print("That class doesn't exist.")
            
        selection=int(input("If you want to select this class type 1 if you want to select another class type 0"))
        if selection==0:
            print("Restarting class information")
            time.sleep(1)
            continue
        elif selection==1:
            own_class=info_class
            print(f"Your class is {own_class} now!!!")
            character_creation()
            break
    


def character_creation():
    ability_points=72
    print("WELCOME TO THE CHARACTER CREATION PAGE !!!!!!")
    time.sleep(2)
    print(f"You have total, {ability_points} ability points")
    time.sleep(3)
    print("You have 5 stats!!!\n Strenght,\n Dexterity,\n Constitition,\n Intelligence,\n,\n Wisdom,\n Charisma")
    time.sleep(3)
    print("You can give to stats these numbers 15,14,13,12,10,8")
    time.sleep(3)
    for stat in stats:
        print(f"\nAvailable numbers: {available}")
        while True:
            choice = input(f"Which number for {stat}? ")
            if not choice.isdigit():
                print("Type a number.")
            elif int(choice) not in available:
                print("That number isn't available.")
            else:
                stats[stat] = int(choice)
                available.remove(int(choice))
                break
    dex_modifier=floor((stats["dex"]-10)/2)
    str_modifier=floor((stats["str"]-10)/2)
    cha_modifier=floor((stats["cha"]-10)/2)
    con_modifier=floor((stats["con"]-10)/2)
    int_modifier=floor((stats["int"]-10)/2)
    wis_modifier=floor((stats["wis"]-10)/2)
    print("And now your modifiers !")
    print(f"Your strenght modifier is:{str_modifier}")
    print(f"Your dexterity modifier is:{dex_modifier}")
    print(f"Your charisma modifier is:{cha_modifier}")
    print(f"Your constitution modifier is:{con_modifier}")
    print(f"Your intelligenc modifier is:{int_modifier}")
    print(f"Your wisdom modifier is:{wis_modifier}")
    
        
    print("AAAND ITS THE END OF THE CHARACHTER CREATIONNNN\n Lets START TO GAME!!!")
    
    
    
    
    
    
    

def equipments():
    print("In that part of game, you can see which eqipments you can have and"
          "some equipment informations for your class")
    time.sleep(2)
    if own_class=="barbarian":
        print("You just have long sword, but because of your class you have insane durability. You can just use light and medium armors.")
        time.sleep(4)
        inventory.append("Light armor")
        print("First of all you have longsword")
        time.sleep(2)
        inventory.append("Longsword") #1d8 attack+modifier
    elif own_class=="druid":
        print("As a druid you can use scimitar i think, THAT'S WHY YOU GOT IT !!!!")
        inventory.append("Scimitar")
    

def spells():
    print("WELCOME TO THE SPELLCASTING MENU!!!!")
    time.sleep(1.5)
    if own_class=="Barbarian" or own_class=="Fighter" or own_class=="Rogue" or own_class=="Monk":
        print("Technically, you have no any spell... BUT NEVERMIND 'CAUSE YOU HAVE DIFFERENT THINGS!!!!")
        time.sleep(3) 
    elif own_class=="Paladin" and level<=2:
        print("You have no spell yet...")
        print("But for now you must skip this page",end="",flush=True)
        for i in range(3):
            print(".",end="",flush=True)
    story()
    
    
    
def story():
    pass    
    
    
    
    
    
def fighting():
    global exp
    while True:
        choose=input("Please choose weapon from inventory")
        time.sleep(2)
        if choose not in inventory:
            print("Please type weapon from YOUR inventory")
            continue
        else:
            break
    while enemy_hp>0:
        dice=random.randint(1,20)
        if dice>=ac:
            roll()
            hp-=dice
            print(f"You hit: {dice}")
            time.sleep(2)
            print(f"Remaining health of enemy is: {hp}")
        dice=random.randint(1,20)
        if dice>=your_ac:
            pass #enemy stats was'nt added yet to the game. i must do that before but i forgot that
    print(f"You won the fight with {enemy_choose}")
    time.sleep(3)
    print(f"You got:{exp} xp!!")
    exp+=monster_exp[enemy_choose]      
            





def roll():
    if choose=="Dagger":
        dice=random.randint(1,4)
        if dex_modifier>str_modifier:
            dice+=dex_modifier
        elif dex_modifier==str_modifier:
            dice+=str_modifier
        else:
            dice+=str_modifier
        print(f"You rolled,{dice}")
        time.sleep(1.5)
        enemy_health-=dice
        print(f"Enemy's hp is, {enemy_health}")
    elif choose=="Handaxe":
        dice=random.randint(1,6)
        dice+=str_modifier
        print(f"You rolled,{dice}")    
        time.sleep(1.5)
        enemy_health-=dice
    elif choose=="Mace":
        dice=random.randint(1,6)
        dice+=str_modifier
        print(f"You rolled,{dice}")
        time.sleep(1.5)
        enemy_health-=dice
    elif choose=="Spear":
        dice=random.randint(1,6)
        dice+=str_modifier
        print(f"You rolled,{dice}")
        time.sleep(1.5)
        enemy_health-=dice
    elif choose=="Shortbow" and arrow>0:
        if dex_modifier>str_modifier:
            dice+=dex_modifier
        elif dex_modifier==str_modifier:
            dice+=dex_modifier
        else:
            dice+=str_modifier
        dice=random.randint(1,6)
        print(f"You rolled,{dice}")
        time.sleep(1.5)
        enemy_health-=dice
    elif choose=="Rapier":
        dice=random.randint(1,8)
        if dex_modifier>str_modifier:
            dice+=dex_modifier
        elif dex_modifier==str_modifier:
            dice+=dex_modifier
        else:
            dice+=dex_modifier
        print(f"You rolled,{dice}")
        time.sleep(1.5)
        enemy_health-=dice
    elif choose=="Longsword":
        dice=random.randint(1,8)
        dice+=str_modifier
        print(f"You rolled,{dice}")
        time.sleep(1.5) 
        enemy_health-=dice
    elif choose=="Greataxe":
        dice=random.randint(1,12)
        dice+=str_modifier
        print(f"You rolled,{dice}")
        time.sleep(1.5)
        enemy_health-=dice
    elif choose=="Greatsword":
        for i in range(2):
            dice=random.randint(1,6)
            dice+=str_modifier
            print(f"You rolled,{dice}")
            total+=dice
            time.sleep(1.5)
            enemy_health-=dice
            print(f"Totally you rolled{total}")
    elif choose=="Light Crossbow":
        dice=random.randint(1,6)
        dice+=dex_modifier
        print(f"You rolled,{dice}")
        time.sleep(1.5)
        enemy_health-=dice
    elif choose=="Heavy crossbow":
        dice+=dex_modifier
        dice=random.randint(1,10)
        print(f"You rolled,{dice}")
        time.sleep(1.5)
        enemy_health-=dice
