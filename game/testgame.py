import os 
def main():
    print("You awake in a bed, you don't remember falling asleep and this definently is not your bed. ")
    while True:
        ChoiceOne = input ("Do you want to: A) Get out of bed. B) Try to fall asleep I must be dreaming. C) Look under bed [A/B/C]? : ")
        if ChoiceOne in ['A', 'B', 'C']:
            break
    if ChoiceOne == "A": 
        print ("you die.")
        A() 
    elif ChoiceOne == "B": 
        print ("you live.")
        B()
    else:
        print ("Uhh bad idea") 
        C()

def A():
    print("Just kidding you find yourself in a library")
    while True:
        ChoiceOne = input ("Do you want to: A) Read a book. B) Talk to the librarian. C) Scream [A/B/C]? : ")
        if ChoiceOne in ['A', 'B', 'C']:
            break
    if ChoiceOne == "A": 
        print ("You black out.") 
    elif ChoiceOne == "B": 
        print ("She was a cardboard cutout.")
    else:
        print ("Shes coming")
    
def B():
    print("You go through your whole life as normal then wake up back in the bed")
    while True:
        ChoiceOne = input ("Do you want to: A) Get out of bed. B) Try to fall asleep I must be dreaming. C) Look under bed [A/B/C]? : ")
        if ChoiceOne in ['A', 'B', 'C']:
            break
    if ChoiceOne == "A": 
        print ("you die.") 
    elif ChoiceOne == "B": 
        print ("you live.")
        B()
    else:
        print ("Uhh bad idea")

def C():
    print("Something grabs you and pulls you under the bed ripping your shoulder out of the socket")
    while True:
        ChoiceOne = input ("Do you want to: A) Wake up its all a dream. B) Open your eyes. C) Try to push your arm back into its socket [A/B/C]? : ")
        if ChoiceOne in ['A', 'B', 'C']:
            break
    if ChoiceOne == "A": 
        print ("You wake up back in the bed.") 
    elif ChoiceOne == "B": 
        print ("You scream.")
    else:
        print ("With a sickining crack your arm goes back into the socket")

Title = (" _     _           _             _   _____                \n"+"| |   (_)         (_)           | | |_   _|               \n"+"| |    _ _ __ ___  _ _ __   __ _| |   | |_   _ _ __   ___ \n"+"| |   | | '_ ` _ \| | '_ \ / _` | |   | | | | | '_ \ / _ \\\n"+"| |___| | | | | | | | | | | (_| | |   | | |_| | |_) |  __/\n"+"\_____/_|_| |_| |_|_|_| |_|\__,_|_|   \_/\__, | .__/ \___|\n"+"                                          __/ | |         \n"+"                                         |___/|_|         ") 
print(Title)
Start = input("press Enter to start") , os.system('cls')
print()
name = input("Hello before we start Id like to get to know you a little bit, what is your name? ")
fear = input("What is your greatest fear? " )
J1 = input(" And finnaly...whats that behind you? " )
print("Haha did you actually look...Okay lets begin "+name)
print()
main()







    #basic framework for question is finished 