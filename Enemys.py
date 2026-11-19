import time
from math import floor
import random
inventory=[]
level=0
from DNDINPYTHON import fighting

def enemies():
    monster_exp = {
    "Bugbear": 200,
    "Giant Spider": 200,
    "Ogre": 450,
    "Gelatinous Cube": 450,
    "Owlbear": 700,
    "Mummy": 700,
    "Banshee": 1100,
    "Chuul": 1100,
    "Bulette": 1800,
    "Troll": 1800,
    "Medusa": 2300,
    "Wyvern": 2300,
    "Mind Flayer": 2900,
    "Oni": 2900,
    "Hydra": 3900,
    "Tyrannosaurus Rex": 3900,
    "Clay Golem": 5000,
    "Treant": 5000,
    "Aboleth": 5900,
    "Young Red Dragon": 5900,
    "Behir": 7200,
    "Efreeti": 7200,
    "Erinyes": 8400,
    "Arcanaloth": 8400,
    "Beholder": 10000,
    "Vampire": 10000,
    "Ice Devil": 11500,
    "Death Tyrant": 11500,
    "Mummy Lord": 13000,
    "Purple Worm": 13000,
    "Adult Blue Dragon": 15000,
    "Planetar": 15000,
    "Death Knight": 18000,
    "Adult Red Dragon": 18000,
    "Demilich": 20000,
    "Dragon Turtle": 18000,
    "Balor": 22000,
    "Lich": 33000,
    "Pit Fiend": 25000,
    "Solar": 33000
}
    print("///////MENU//////")
    time.sleep(1)
    print(f"Your level is,{level} you can choose every level of enemy but please" 
          "\n choose enemies that you can defeat for real, except you will die!")
    def level_1_enemies():
        print("There have 2 one level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Bugbear\n 2.Giant Spider")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            bugbear()
        elif enemy_choose==2:
            giant_spider()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def bugbear():
            print("You've seen bugbear ever?",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            print("I don’t know, but you saw it this time.")
            ac=16
            enemy_hp=27
            fighting()
            for i in range(2):
                dice=random.randint(1,6)
                total_gp+=dice
            if random.randint(1,100)>=60:
                item="Morning Star"
                print(f"YOU GOT {item} !!!!\n Congratulations dear player!")
                inventory.append(item)
            elif random.randint(1,100)>=50:
                item="Javelin"
                print(f"YOU GOT {item} !!!! \n Congratulations dear player!")
                inventory.append(item)
            elif random.randint(1,100)>=15:
                item="Potion of Healing"
                print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                inventory.append(item)
                
            
        def giant_spider():
            print("Have you ever seen a giant spider??")
            time.sleep(2)
            print("“You can hear the giant spider’s pincers clicking as it walks.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=14
            hp=26
            fighting()
            if random.randint(1,100)>=70:
                item="Spider silk"
                print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                inventory.append(item)
            elif random.randint(1,100)>=40:
                item="Poison gland" #it is 25gp
                print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                inventory.append(item)
            elif random.randint(1,100)>=35:
                item="victim's coin pouch" #1d10 gp
                print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                dice=random.randint(1,10)
                total_gp+=dice
    def level_2_enemies():
        print("There have 2 two level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Ogre\n 2.Gelatinous Cube")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            ogre()
        elif enemy_choose==2:
            gelatinous_cube()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def ogre():
            print("Have you ever seen an ogre??")
            time.sleep(2)
            print("“Something huge is stomping toward you.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=11
            enemy_hp=59
            fighting()
            if enemy_hp<=0:
                for i in range(3):
                    dice=random.randint(1,6)
                    total_gp+=dice
                if random.randint(1,100)>=70:
                    item="Greatclub"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Sack of junk" #it is 10gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=20:
                    item="Potion of Healing"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def gelatinous_cube():
            print("Have you ever seen a gelatinous cube??")
            time.sleep(2)
            print("“The air ahead of you wobbles like jelly.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=6
            enemy_hp=84
            fighting()
            if enemy_hp<=0:
                for i in range(2):
                    dice=random.randint(1,10)
                    total_gp+=dice
                if random.randint(1,100)>=40:
                    item="Rusted shortsword"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=25:
                    item="Gem" #it is 10gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=5:
                    item="+1 Dagger"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_3_enemies():
        print("There have 2 three level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Owlbear\n 2.Mummy")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            owlbear()
        elif enemy_choose==2:
            mummy()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def owlbear():
            print("Have you ever seen an owlbear??")
            time.sleep(2)
            print("“You hear a screech and heavy claws on the stone.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=13
            enemy_hp=59
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=80:
                    item="Owlbear pelt" #it is 30gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Bones in den"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(1):
                        dice=random.randint(1,10)
                        total_gp+=dice
                elif random.randint(1,100)>=15:
                    item="Potion of Healing"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def mummy():
            print("Have you ever seen a mummy??")
            time.sleep(2)
            print("“Dust falls from the ceiling as old bandages rustle.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=11
            enemy_hp=58
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=80:
                    item="Burial jewelry" #it is 5d6 gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=25:
                    item="Scroll of 1st level spell"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=3:
                    item="Ring of Protection"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_4_enemies():
        print("There have 2 four level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Banshee\n 2.Chuul")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            banshee()
        elif enemy_choose==2:
            chuul()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def banshee():
            print("Have you ever seen a banshee??")
            time.sleep(2)
            print("“A cold wail echoes through the room.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=12
            enemy_hp=58
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=90:
                    item="Fine jewelry" #it is 4d10 gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=30:
                    item="Silver mirror shard" #it is 50gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=20:
                    item="Scroll of 2nd level spell"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def chuul():
            print("Have you ever seen a chuul??")
            time.sleep(2)
            print("“Something wet and clawed rises out of the water.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=16
            enemy_hp=93
            fighting()
            if enemy_hp<=0:
                for i in range(4):
                    dice=random.randint(1,10)
                    total_gp+=dice
                if random.randint(1,100)>=50:
                    item="Gem" #it is 50gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=30:
                    item="Potion of Healing"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=8:
                    item="+1 Weapon"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_5_enemies():
        print("There have 2 five level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Bulette\n 2.Troll")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            bulette()
        elif enemy_choose==2:
            troll()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def bulette():
            print("Have you ever seen a bulette??")
            time.sleep(2)
            print("“The ground shakes and a fin cuts through the dirt.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=17
            enemy_hp=94
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=70:
                    item="Armor plates" #it is 100gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=60:
                    item="Coins in its gut"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(4):
                        dice=random.randint(1,20)
                        total_gp+=dice
                elif random.randint(1,100)>=20:
                    item="Potion of Greater Healing"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def troll():
            print("Have you ever seen a troll??")
            time.sleep(2)
            print("“You smell something rotten and it is getting closer.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=15
            enemy_hp=84
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=80:
                    item="Bag of coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(5):
                        dice=random.randint(1,10)
                        total_gp+=dice
                elif random.randint(1,100)>=60:
                    item="Adventurer gear"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=25:
                    item="Potion of Greater Healing"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=6:
                    item="+1 Armor"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_6_enemies():
        print("There have 2 six level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Medusa\n 2.Wyvern")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            medusa()
        elif enemy_choose==2:
            wyvern()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def medusa():
            print("Have you ever seen a medusa??")
            time.sleep(2)
            print("“Whatever you do, do not look into her eyes.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=15
            enemy_hp=127
            fighting()
            if enemy_hp<=0:
                for i in range(6):
                    dice=random.randint(1,20)
                    total_gp+=dice
                if random.randint(1,100)>=60:
                    item="Jeweled longbow" #it is 150gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Gem" #it is 100gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=25:
                    item="Scroll of 3rd level spell"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=10:
                    item="Uncommon magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def wyvern():
            print("Have you ever seen a wyvern??")
            time.sleep(2)
            print("“Leathery wings block out the sky.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=13
            enemy_hp=110
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=70:
                    item="Venom vial" #it is 200gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Nest coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(5):
                        dice=random.randint(1,20)
                        total_gp+=dice
                elif random.randint(1,100)>=20:
                    item="Potion of Greater Healing"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_7_enemies():
        print("There have 2 seven level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Mind Flayer\n 2.Oni")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            mind_flayer()
        elif enemy_choose==2:
            oni()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def mind_flayer():
            print("Have you ever seen a mind flayer??")
            time.sleep(2)
            print("“A strange voice whispers inside your head.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=15
            enemy_hp=71
            fighting()
            if enemy_hp<=0:
                for i in range(6):
                    dice=random.randint(1,20)
                    total_gp+=dice
                if random.randint(1,100)>=40:
                    item="Breastplate"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=60:
                    item="Gem" #it is 100gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=15:
                    item="Uncommon wand"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=10:
                    item="+1 Weapon"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def oni():
            print("Have you ever seen an oni??")
            time.sleep(2)
            print("“A giant with a glaive laughs in the dark.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=16
            enemy_hp=110
            fighting()
            if enemy_hp<=0:
                for i in range(7):
                    dice=random.randint(1,20)
                    total_gp+=dice
                if random.randint(1,100)>=15:
                    item="+1 Magic glaive"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Stolen jewelry" #it is 150gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=15:
                    item="Potion of Superior Healing"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_8_enemies():
        print("There have 2 eight level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Hydra\n 2.Tyrannosaurus Rex")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            hydra()
        elif enemy_choose==2:
            tyrannosaurus_rex()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def hydra():
            print("Have you ever seen a hydra??")
            time.sleep(2)
            print("“Many heads rise from the swamp and all of them are hungry.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=15
            enemy_hp=172
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=60:
                    item="Hydra scales" #it is 300gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=60:
                    item="Victims' coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(8):
                        dice=random.randint(1,20)
                        total_gp+=dice
                elif random.randint(1,100)>=40:
                    item="Gem" #it is 100gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=20:
                    item="Potion of Superior Healing"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def tyrannosaurus_rex():
            print("Have you ever seen a tyrannosaurus rex??")
            time.sleep(2)
            print("“The ground shakes with every step it takes.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=13
            enemy_hp=136
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=70:
                    item="Giant teeth" #it is 250gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Hide" #it is 200gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=40:
                    item="Swallowed gear"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(4):
                        dice=random.randint(1,20)
                        total_gp+=dice
                elif random.randint(1,100)>=6:
                    item="+1 Armor"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_9_enemies():
        print("There have 2 nine level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Clay Golem\n 2.Treant")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            clay_golem()
        elif enemy_choose==2:
            treant()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def clay_golem():
            print("Have you ever seen a clay golem??")
            time.sleep(2)
            print("“A statue made of clay opens its eyes.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=14
            enemy_hp=133
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=60:
                    item="Quality clay" #it is 200gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=30:
                    item="Amulet" #it is 300gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=15:
                    item="Scroll of 4th level spell"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def treant():
            print("Have you ever seen a treant??")
            time.sleep(2)
            print("“You thought it was a tree until it moved.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=16
            enemy_hp=138
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=70:
                    item="Heartwood" #it is 400gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=30:
                    item="Acorn (potion of growth)"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=10:
                    item="Uncommon staff"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_10_enemies():
        print("There have 2 ten level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Aboleth\n 2.Young Red Dragon")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            aboleth()
        elif enemy_choose==2:
            young_red_dragon()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def aboleth():
            print("Have you ever seen an aboleth??")
            time.sleep(2)
            print("“The water in the lake starts to glow.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=17
            enemy_hp=135
            fighting()
            if enemy_hp<=0:
                for i in range(10):
                    dice=random.randint(1,20)
                    total_gp+=dice
                if random.randint(1,100)>=60:
                    item="Sunken gems" #it is 500gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=30:
                    item="Uncommon magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=8:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def young_red_dragon():
            print("Have you ever seen a young red dragon??")
            time.sleep(2)
            print("“You feel the heat long before you see the fire.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=18
            enemy_hp=178
            fighting()
            if enemy_hp<=0:
                for i in range(10):
                    dice=random.randint(1,20)
                    total_gp+=dice
                if random.randint(1,100)>=60:
                    item="Gems" #it is 500gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=40:
                    item="Uncommon magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=10:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_11_enemies():
        print("There have 2 eleven level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Behir\n 2.Efreeti")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            behir()
        elif enemy_choose==2:
            efreeti()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def behir():
            print("Have you ever seen a behir??")
            time.sleep(2)
            print("“Lightning crackles along a long serpent body.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=17
            enemy_hp=168
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=70:
                    item="Lightning-scale hide" #it is 600gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=60:
                    item="Coin pile"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(6):
                        dice=random.randint(1,20)
                        total_gp+=dice
                elif random.randint(1,100)>=50:
                    item="Swallowed gear"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=8:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def efreeti():
            print("Have you ever seen an efreeti??")
            time.sleep(2)
            print("“A burning figure steps out of the smoke.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=17
            enemy_hp=200
            fighting()
            if enemy_hp<=0:
                for i in range(2):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=80:
                    item="Jeweled scimitar" #it is 500gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=40:
                    item="Uncommon magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=12:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_12_enemies():
        print("There have 2 twelve level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Erinyes\n 2.Arcanaloth")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            erinyes()
        elif enemy_choose==2:
            arcanaloth()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def erinyes():
            print("Have you ever seen an erinyes??")
            time.sleep(2)
            print("“Black wings and a sword of fire appear above you.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=18
            enemy_hp=153
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=50:
                    item="+1 Longsword and longbow"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=40:
                    item="Plate armor"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=80:
                    item="Bag of coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(2):
                        dice=random.randint(1,6)
                        total_gp+=dice*100
                elif random.randint(1,100)>=10:
                    item="Rope of entanglement"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def arcanaloth():
            print("Have you ever seen an arcanaloth??")
            time.sleep(2)
            print("“A cold voice offers you a very bad deal.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=17
            enemy_hp=104
            fighting()
            if enemy_hp<=0:
                for i in range(2):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=60:
                    item="Spellbook" #it is 800gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=25:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=30:
                    item="Scroll of 5th level spell"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_13_enemies():
        print("There have 2 thirteen level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Beholder\n 2.Vampire")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            beholder()
        elif enemy_choose==2:
            vampire()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def beholder():
            print("Have you ever seen a beholder??")
            time.sleep(2)
            print("“A giant floating eye looks right at you.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=18
            enemy_hp=180
            fighting()
            if enemy_hp<=0:
                for i in range(3):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=60:
                    item="Gems" #it is 1000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=35:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=8:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def vampire():
            print("Have you ever seen a vampire??")
            time.sleep(2)
            print("“A pale noble smiles and shows his teeth.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=16
            enemy_hp=144
            fighting()
            if enemy_hp<=0:
                for i in range(3):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=80:
                    item="Noble jewelry" #it is 1500gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=20:
                    item="Cloak of Protection"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=8:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_14_enemies():
        print("There have 2 fourteen level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Ice Devil\n 2.Death Tyrant")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            ice_devil()
        elif enemy_choose==2:
            death_tyrant()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def ice_devil():
            print("Have you ever seen an ice devil??")
            time.sleep(2)
            print("“The room freezes and your breath turns white.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=18
            enemy_hp=180
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=10:
                    item="+2 Ice spear"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=70:
                    item="Bag of coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(3):
                        dice=random.randint(1,6)
                        total_gp+=dice*100
                elif random.randint(1,100)>=50:
                    item="Frozen gems" #it is 800gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=25:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def death_tyrant():
            print("Have you ever seen a death tyrant??")
            time.sleep(2)
            print("“A dead floating eye drifts toward you.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=19
            enemy_hp=187
            fighting()
            if enemy_hp<=0:
                for i in range(3):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=40:
                    item="Preserved rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=12:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_15_enemies():
        print("There have 2 fifteen level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Mummy Lord\n 2.Purple Worm")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            mummy_lord()
        elif enemy_choose==2:
            purple_worm()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def mummy_lord():
            print("Have you ever seen a mummy lord??")
            time.sleep(2)
            print("“An ancient king rises from his tomb.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=17
            enemy_hp=97
            fighting()
            if enemy_hp<=0:
                for i in range(4):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=90:
                    item="Royal regalia" #it is 3000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=40:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=12:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def purple_worm():
            print("Have you ever seen a purple worm??")
            time.sleep(2)
            print("“The whole cave shakes and a huge mouth opens.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=18
            enemy_hp=247
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=80:
                    item="Gems and metals" #it is 2000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=70:
                    item="Bag of coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(4):
                        dice=random.randint(1,6)
                        total_gp+=dice*100
                elif random.randint(1,100)>=8:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_16_enemies():
        print("There have 2 sixteen level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Adult Blue Dragon\n 2.Planetar")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            adult_blue_dragon()
        elif enemy_choose==2:
            planetar()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def adult_blue_dragon():
            print("Have you ever seen an adult blue dragon??")
            time.sleep(2)
            print("“Lightning strikes the ground in front of you.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=19
            enemy_hp=225
            fighting()
            if enemy_hp<=0:
                for i in range(5):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=70:
                    item="Gems" #it is 2500gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=15:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def planetar():
            print("Have you ever seen a planetar??")
            time.sleep(2)
            print("“A shining angel looks down at you.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=19
            enemy_hp=200
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=10:
                    item="+2 Greatsword"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Bag of coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(5):
                        dice=random.randint(1,6)
                        total_gp+=dice*100
                elif random.randint(1,100)>=50:
                    item="Gem" #it is 1000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=20:
                    item="Scroll of 6th level spell"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=10:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_17_enemies():
        print("There have 2 seventeen level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Death Knight\n 2.Adult Red Dragon")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            death_knight()
        elif enemy_choose==2:
            adult_red_dragon()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def death_knight():
            print("Have you ever seen a death knight??")
            time.sleep(2)
            print("“A knight in black armor draws his sword.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=20
            enemy_hp=180
            fighting()
            if enemy_hp<=0:
                for i in range(6):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=30:
                    item="+1 Plate armor"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=10:
                    item="+2 Longsword"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=20:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def adult_red_dragon():
            print("Have you ever seen an adult red dragon??")
            time.sleep(2)
            print("“The mountain burns and a huge shadow flies over it.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=19
            enemy_hp=256
            if enemy_hp<=0:
                for i in range(6):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=70:
                    item="Gems" #it is 5000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=40:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=5:
                    item="Legendary magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_18_enemies():
        print("There have 2 eighteen level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Demilich\n 2.Dragon Turtle")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            demilich()
        elif enemy_choose==2:
            dragon_turtle()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def demilich():
            print("Have you ever seen a demilich??")
            time.sleep(2)
            print("“A skull floats in the dark and whispers your name.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=20
            enemy_hp=80
            fighting()
            if enemy_hp<=0:
                for i in range(8):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                dice=random.randint(1,4)
                for i in range(dice):
                    item="Soul Gem" #it is 1500gp each
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                if random.randint(1,100)>=35:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=8:
                    item="Legendary magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def dragon_turtle():
            print("Have you ever seen a dragon turtle??")
            time.sleep(2)
            print("“The sea rises and a shell bigger than a ship appears.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=20
            enemy_hp=341
            fighting()
            if enemy_hp<=0:
                for i in range(8):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=60:
                    item="Pearls" #it is 5000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=30:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_19_enemies():
        print("There have 2 nineteen level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Balor\n 2.Lich")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            balor()
        elif enemy_choose==2:
            lich()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def balor():
            print("Have you ever seen a balor??")
            time.sleep(2)
            print("“A wall of fire and a whip made of flame.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=19
            enemy_hp=262
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=10:
                    item="Flame whip" #it is rare
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=70:
                    item="Bag of coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(8):
                        dice=random.randint(1,6)
                        total_gp+=dice*100
                elif random.randint(1,100)>=60:
                    item="Gems" #it is 5000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=40:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=6:
                    item="Legendary magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


        def lich():
            print("Have you ever seen a lich??")
            time.sleep(2)
            print("“The air gets cold and a quiet voice laughs.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=17
            enemy_hp=135
            fighting()
            if enemy_hp<=0:
                for i in range(10):
                    dice=random.randint(1,6)
                    total_gp+=dice*100
                if random.randint(1,100)>=90:
                    item="Spellbook" #it is 5000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=15:
                    item="Legendary magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)


    def level_20_enemies():
        print("There have 2 twenty level enemy, please choose one of them or type 0 for exit from the program")
        print("1.Pit Fiend\n 2.Solar")
        enemy_choose=input()
        enemy_choose.lower()
        time.sleep(1.5)
        if enemy_choose==1:
            pit_fiend()
        elif enemy_choose==2:
            solar()
        else:
            print("Returning to the menu, Please wait")
            print("Loading",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
                enemies()
        def pit_fiend():
            print("Have you ever seen a pit fiend??")
            time.sleep(2)
            print("“The ground cracks and the whole place smells like fire.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=19
            enemy_hp=300
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=15:
                    item="+2 Mace"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=80:
                    item="Bag of coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(10):
                        dice=random.randint(1,6)
                        total_gp+=dice*100
                elif random.randint(1,100)>=60:
                    item="Gems" #it is 8000gp
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=50:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=12:
                    item="Legendary magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)

        def solar():
            print("Have you ever seen a solar??")
            time.sleep(2)
            print("“A blinding angel with a bow made of light.”")
            time.sleep(3)
            print("Maybe this time you will see it",end="",flush=True)
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            ac=21
            enemy_hp=243
            fighting()
            if enemy_hp<=0:
                if random.randint(1,100)>=20:
                    item="Slaying longbow" #it is very rare
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=70:
                    item="Bag of coins"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    for i in range(10):
                        dice=random.randint(1,6)
                        total_gp+=dice*100
                elif random.randint(1,100)>=60:
                    item="Very rare magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)
                elif random.randint(1,100)>=20:
                    item="Legendary magic item"
                    print(f"YOU GOT {item}!!!!\n Congratulations dear player!")
                    inventory.append(item)