# i am making this out of spite
#import routines.accessories
#import routines.actions
import random
import routines.targets
from game import Game
from area import Area
VERSION = "Early Alpha"


#basic start menu
def start_menu():
    print("1.about\n2.instructions\n3.play game")
    match input("input: "):
        case "1":
            print("SELENE is a moon mission over text. \nIt is created by Vicky Yang, Jade Lukken, and Devin Foster for CS 1612 at the University of Minnesota Duluth")
            start_menu()
        case "2":
            print("When prompted, type commands into the console and press ENTER. \nThese commands include:\nmove {location name}\npush {button name}\nand fix {object}")
            print("The \"map\" command draws a map in the turtle window. NOTE: Map window cannot be closed by player using window close button. \nTo exit the game, player must hit ctrl-c and then enter.")
            print("Try and experiment with potential commands to see if they work in potential situtations!")
            print("Paper and pencil is recommended to have on hand.")
            start_menu()
        case "3":
            return
        case _:
            print("input a correct input")
            start_menu()



        
   
#driver code
from routines.targets import button
oxygenTubeFixed = False
launchReady = False
BUTTON_DICT = {"jdry" : button, "uo13" : button, "vk88" : button, "jn34" : button, "wz81" : button, "vo29" : button, "fk73" : button, "kj22" : button, "mo11" : button, "we64" : button, "lq12" : button, "ii43" : button, "js01" : button, "cf04" : button, "sz24" : button, "ez59" : button, "n57x" : button, "msy4" : button, "aym1" : button, "0frz" : button, "dyjj" : button, "jv71" : button, "4lhm" : button, "fdcx" : button, "ut9c" : button, "8rsl" : button, "ra78" : button, "jmn8" : button, "rwb5" : button, "xuu6" : button, "sgub" : button, "awpz" : button, "rrdz" : button, "mdna" : button, "wa03" : button, "ut13" : button, "zo51" : button, "ef57" : button, "uj34" : button, "su33" : button}

#area creation
cape = Area(["cape", "mission control"], "this is cape canveral, the starting point in your journey", [], mapPath="savedshapes/capemap.json")
tower = Area(["tower", "pad"], "this is tower", [], mapPath="savedshapes/towermap.json")
capsule = Area(["capsule", "inside"], "this is the space capsule", [], {"launchReady" : launchReady}, mapPath="savedshapes/capsulemap.json")
dockingPort = Area(["docking port", "dock"], "you are next to the [docking port], out in space. the broken oxygen tube is right in front of you.", [], {"fixed" : oxygenTubeFixed}, mapPath="savedshapes/capsulemap.json")
outsideCapsuleDoor = Area(["outside capsule door", "outside", "spacewalk", "space", "capsule door"], "you are out in space next to the [capsule door]. the broken oxygen tube is right next to the [docking port]", [], mapPath="savedshapes/capsulemap.json")
capsule.avaliable_targets = BUTTON_DICT 
dockingPort.avaliable_targets = {}
capsule.gates = outsideCapsuleDoor.names + cape.names + tower.names
dockingPort.gates = outsideCapsuleDoor.names
outsideCapsuleDoor.gates = capsule.names + dockingPort.names
cape.gates = capsule.names + tower.names
tower.gates = capsule.names + cape.names



AREA_DICT = {"capsule" : capsule, "inside" : capsule, 
             "outside" : outsideCapsuleDoor, "spacewalk" : outsideCapsuleDoor, "space" : outsideCapsuleDoor, "capsule door" : outsideCapsuleDoor,
             "docking port" : dockingPort, "dock" : dockingPort,
             "cape" : cape, "mission control" : cape,
             "tower" : tower}

game = Game(capsule)
Game.AREA_DICT = AREA_DICT

def fire_put_out_sequence():
    fire_health = 50
    ventilator_off = False

    while fire_health > 0:
        action = input("A fire has broken out! Do you want to (1) Turn off ventilators, (2) Use CO2 extinguisher, or (3) Throw water on it? ")
        if action == "1" and not ventilator_off:
            ventilator_off = True
            print("You turned off the ventilators. No more oxygen is feeding the fire.")
        elif action == "2" and ventilator_off:
            damage = random.randint(10, 20)
            fire_health -= damage
            print(f"You used the CO2 extinguisher and dealt {damage} damage. Fire health is now {fire_health}.")
            if fire_health <= 0:
                print("You successfully put out the fire!")
                break
        elif action == "3":
            print("Throwing water on an electrical fire was a bad idea! You got electrocuted. Game over.")
            break
        elif action == "1" and ventilator_off:
            print("The ventilators are already off. Wrong action! You burned to death. Game over.")
            break
        else:
            print("Wrong action! You burned to death. Game over.")
            break


print("SELENE " + str(VERSION))

start_menu()
fire_put_out_sequence()
#basic starting senario
print("you are just about to do your moon burn calculations that will put you in the moons orbit!")
game.add_radio_notification("you see the \"incomming message\" light fire on your dashboard", "HOUSTON: we've detected a leak in one of the oxygen tubes out by the dock. please go out and fix it before you get ready for launch!")
while not Game.gameOver:
    game.player_input()
    if Game.incorrectButtonPresses >= 2:
        print("your engines suddenly misfire and blow up your capsule. it's a sad day for spaceflight. :(")
        print("game over...")
        Game.gameOver = True

# Fire Put Out Sequence


