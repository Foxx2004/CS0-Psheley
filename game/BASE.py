def blank_module():
         
    """Put room image here()""", print (
 #                                                                                      for normal text line--->|  |<-- place here for """ #
"""| Write Text here                                                                                               |
|                                                                                                               |""")
              
    while True:

        print(
"""|                                                                                                               |
| Write visable choices here                                                                                    |
|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------""")
        ChoiceOne = input("what do you do: ")

        if ChoiceOne in ['A', 'B', 'C', 'Non-visable choice']: 
            break
    if ChoiceOne == "A": 
        """RoomFunction()"""
    
    elif ChoiceOne == "B": 
        """RoomFunction()"""

    elif ChoiceOne == "C": 
        """RoomFunction()"""

    elif ChoiceOne == "Non-visable choice": 
        """RoomFunction()"""

    
def Blank_art():
     os.system("cls")
     print(R""" """)




def DecisonPA():# makes it so cant keep getting item over and over
    global item

    if item == False:    
        print (
""" type what happens if they dont already have item""")
        DecisonPB()

    else: input(
""" type what happens if they do already have item""") 
    os.system("cls")
    Room_currently_in() 

def DecisonPB():
    global item
    global item2
          

 #                                                                                      for normal text line--->|  |<-- place here for """ 
    while True:

        print(
"""-----------------------------------------------------------------------------------------------------------------""")
        ChoiceOne = input("Let them decide if they want to attempt to get item ")

        if ChoiceOne in ['Y','N']: 
            break

        
    if ChoiceOne == "N": 
        os.system("cls") 
        Room() #type what room they are currently end
    
    elif item1 == True and item2 == False : # only lets you get item if you already have one
        axe = True  
        print(
"""Type how they get           
                                                                                                               
-----------------------------------------------------------------------------------------------------------------""")
    
        input("type you got "item")
        os.system("cls")
        Room()

    elif ChoiceOne == "Y" and knife == False: 
        input("type what happens if you dont have the right item with you")
        os.system("cls")
        Room()
