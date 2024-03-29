import os 
import time
from animations_Game import *

key = False
axe = False
knife = False
window = False

def main():
    Title()
    RoomOne(), print (
 #                                                                                      for normal text line--->|  |<-- place here for """ #
"""| You were going through just another regular day. You see the same people and do the same things,              |
| just as always. In a moment of weakness, or maybe you just not having enough sleep, you find yourself         |
| nodding off. Sounding as if echoing in a large steel tube, you hear someone call your name! You immediately   |
| shoot up out of the trance you were stuck in and look around. When before you were in familiar                |
| mundane surroundings, you were now somewhere completely different. Looking around you were in a small         |
| dilapidated bedroom. The air stunk of mold and rot; the very walls seemed to rise and fall,                   |
| almost like breaths of air flowing through them. There is a BED long since forgotten,                         |
| turning around you see Three doors in front of you: one on the Left, one on the Right, and one in the Middle. |""")
    while True:
        print(
"""|                                                                                                               |
| A: Go through door on the Left. B: Go through door on the Right. C: Go through Middle door.                   |
|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------""")
        ChoiceOne = input("what do you do: ")

        if ChoiceOne in ['A', 'B', 'C', 'BED']: 
            break
    if ChoiceOne == "A": 
        walkingAnimation()
        Left()
    
    elif ChoiceOne == "B": 
        walkingAnimation()
        Right()

    elif ChoiceOne == "C": 
        walkingAnimation()
        Middle()

    elif ChoiceOne == "BED": 
        Under_bed()
    

        
def Bedroom():
    
    RoomOne(), print (
 #                                                                                      for normal text line--->|  |<-- place here for """ #
"""| Looking at the bedroom, you are met with the same forgotten BED and the same moving walls. In the back        | 
| corner of the bedroom, you see a large steel door, with red hand prints all around it. There is a bloodied    |
| KEYPAD next to it. You turn back around to the three dark hallways.                                           |""")
    while True:
        print(
"""|                                                                                                               |
| A: Go through door on the Left. B: Go through door on the Right. C: Go through Middle door.                   |
|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------""")
        ChoiceOne = input("what do you do: ")

        if ChoiceOne in ['A', 'B', 'C', 'BED', 'KEYPAD']: 
            break
    if ChoiceOne == "A": 
        walkingAnimation()
        Left()
    
    elif ChoiceOne == "B": 
        walkingAnimation()
        Right()

    elif ChoiceOne == "C": 
        walkingAnimation()
        Middle()

    elif ChoiceOne == "BED": 
        Under_bed()

    elif ChoiceOne == "KEYPAD": 
            walkingAnimation()
    
   
        

def Left():

    Kitchen(), print (
 #                                                                                      for normal text line--->|  |<-- place here for """ #
"""| Coming out of the hallway, you are hit with the most rancid, putrid smell; looking around, you see that you   | 
| are in a small disgusting kitchen. The ground and walls are covered in some sort of black substance that      | 
| smells of decay. You stifle back a gag as you feel your lunch start to come back up. Looking around you see a |
| Fridge covered with rust and mold, in the back of the kitchen there is a BOARDED UP DOOR, it sounds as if     |
| something is scratching on the other side. The sound of thousands of little legs hits your ears as you        |
| realize that the black substance covering the kitchen is thousands and thousands of cockroaches moving        |
| in unison. You better not linger here long or face being their next meal.                                     |""")
              
    while True:

        print(
"""|                                                                                                               |
| A: Go back to the Bedroom. B: Walk over to the Fridge. C: Plunge your hands deep into the cockroaches.        |
|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------""")
        ChoiceOne = input("what do you do: ")

        if ChoiceOne in ['A', 'B', 'C', 'BOARDED UP DOOR']: 
            break
    if ChoiceOne == "A": 
        walkingAnimation()
        Bedroom()
    
    elif ChoiceOne == "B": 
        walkingAnimation()
        """RoomFunction()"""

    elif ChoiceOne == "C": 
        walkingAnimation()
        """RoomFunction()"""
    
    elif ChoiceOne == "BOARDED UP DOOR": 
        walkingAnimation()
        """RoomFunction()"""
        



def Right():
         
    LivingRoom(), print (
 #                                                                                      for normal text line--->|  |<-- place here for """ #
"""| Taking the right path you come to a large room with a COUCH, this must be the living room. It's extremely     | 
| quiet here all you can hear is the soft sound of rain on the old sliding WINDOW on the far wall. Each step    | 
| you take in the room creates plumes of dust that sparkle in the sterilizing yellow light of the room.         | 
| Opposite the couch is a small desk with an old dusty computer sitting on top.                                 |""")
              
    while True:

        print(
"""|                                                                                                               |
| A: Go back to the Bedroom. B: Go over to the computer. C: Turn off the awful yellow light.                    |
|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------""")
        ChoiceOne = input("what do you do: ")

        if ChoiceOne in ['A', 'B', 'C', 'COUCH', "WINDOW"]: 
            break
    if ChoiceOne == "A": 
        walkingAnimation()
        Bedroom()
    
    elif ChoiceOne == "B": 

        walkingAnimation()
        """RoomFunction()"""

    elif ChoiceOne == "C": 
        walkingAnimation()
        """RoomFunction()"""

    elif ChoiceOne == "COUCH": 
        Couch()

    elif ChoiceOne == "WINDOW": 
        WindowOpen()
    



def Middle():
         
    BackYard(), print (
 #                                                                                      for normal text line--->|  |<-- place here for """ #
"""| You emerge in what looks to be a backyard but the sky above is pitch black, with no stars, no light just the  |
| sound of wind whipping by your ears. At the back of the fence, there is an old wood SHED with a slightly      | 
| familiar melody emanating from inside. There are thick square bushes up against the fence on the right with   |
| shimmering red berries attached to them. Right as you were about to decide what to do a bright light          | 
| illuminated the sky causing you to shield your eyes in pain. Once your eyes had adjusted you saw that         |
| the once-black sky was now blood red.                                                                         |""")
              
    while True:

        print(
"""|                                                                                                               |
| A: Go back to the Bedroom. B: Go over to the bushes. C: Stair into the blood red sky.                         |
|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------""")
        ChoiceOne = input("what do you do: ")

        if ChoiceOne in ['A', 'B', 'C', 'Non-visable choice']: 
            break
    if ChoiceOne == "A": 
        walkingAnimation()
        Bedroom()
    
    elif ChoiceOne == "B": 

        walkingAnimation()
        """RoomFunction()"""

    elif ChoiceOne == "C": 
        walkingAnimation()
        """RoomFunction()"""

    elif ChoiceOne == "Non-visable choice": 
        walkingAnimation()
        """RoomFunction()"""
    


def Under_bed():
    global knife
         
    UBED(), print (
"""| You walk over to the bed, crouching down you hear a shift in the floorboards under the bed.                   |""") 
 #                                                                                      for normal text line--->|  |<-- place here for """ 
    while True:

        print(
"""|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------""")
        ChoiceOne = input("Do you stick your hand in and feel around: [Y/N]? ")

        if ChoiceOne in ['Y','N']: 
            break
    if ChoiceOne == "N": 
        os.system("cls")
        Bedroom()
    
    elif knife == False:
        knife = True  
        print(
"""Reaching into the darkness you feel something grab your hand, you start to panic but you feel something
place a cold object into your hand. You pull your hand out and see that you now have a rusty metal            
Scalpel in your hand.                                                                                         
                                                                                                               
-----------------------------------------------------------------------------------------------------------------""")
    
        input("You got a Scalple!")
        os.system("cls")
        Bedroom()

    else:
        input("You dont dare put your hand under the bed again")
        os.system("cls")
        Bedroom()


main()