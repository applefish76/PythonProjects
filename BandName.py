print("Welcome to my Band name generator LOL! \nFirstly, just a few questions for you :)")

name = input("What is your name? \n")
print("Ok " + name + "! Let's generate you a band name!")

emotional_State = input("How are you feeling today? \n")

animal = input("What's your favorite animal? \n")

colour = input("What is your favorite colour? \n")
Band_Name = ("The " + emotional_State + " " +  colour + " " + animal + "'s!")

print("Great! I have enough info to generate your band name.... \nYour band name is...\n " " \n" + Band_Name)
Yes_or_No = input("Would you like to know the number of characters in your band name? \n")

if Yes_or_No == "yes":print(str(len(Band_Name)-3) + "\nThanks for playing! :)")
else:print("Thank's for playing :)")

