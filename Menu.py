import time
from DNDINPYTHON import character_creation
from DNDINPYTHON import class_pick_session
def menu():
    print("//////MENU//////")
    time.sleep(2)
    print("WELCOME TO THE MAIN MENU!!!!")
    time.sleep(1.5)
    print("This is dnd based game ! have a fun!")
    print("1-start the game")
    print("2-information about game")
    print("0-exit from the game")
    choose=int(input("type now."))
    if choose==1:
        print("Game is loading",end="",flush=True)
        for i in range(3):
            print(".",end="",flush=True)
            time.sleep(1)
        class_pick_session()
    elif choose==2:
        character_creation()
    elif choose==0:
        print("Leaving from the game ! Have a good day dear user",end="",flush=True)
        for i in range(3):
            print(".",end="",flush=True)
        exit()
menu()