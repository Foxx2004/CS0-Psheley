print("You awake in a bed, you don't remember falling asleep and this definently is not your bed. ")
while True:
    ChoiceOne = input ("Do you want to: A) Get out of bed. B) Try to fall asleep I must be dreaming. C) Look under bed [A/B/C]? : ")
    if ChoiceOne in ['A', 'B', 'C']:
        break
if ChoiceOne == "A": 
    print ("you die.") 
elif ChoiceOne == "B": 
    print ("you live.")
elif ChoiceOne == "C":
    print ("Uhh bad idea")









    #basic framework for question is finished 