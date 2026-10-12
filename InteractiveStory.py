

print(r'''
          /\          /\          /\
         /  \        /  \        /  \
        / /\ \      / /\ \      / /\ \
       | |##| |    | |##| |    | |##| |
    ___| |_/|_|____| |_/|_|____| |_/|_|___
   /   |  \\//  |  |  \\//  |  |  \\//  |   \
  |    |___||___|  |___||___|  |___||___|    |
  |   /  / || \  \   /  / || \  \   /  / || \  \ 
  |  |  |  ||  |  ||  |  ||  |  |  ||  |  ||  |  |
  |  |   \----/   | |   \----/   | |   \----/   |
  |  |       ---------------------         ___ |
  |  |      [          |          ]       | . |
  |  |      [          |          ]       |  |
  |  |      [        . |  .       ]         |
  |__|      [          |          ]   |__|
    \     ~~~  ~~~   ~~~    ~~~   ~~~    /
     \    \    \    \    /    /    /    /
      \    \    \    \  /    /    /    /
       '---------------------------------'
''')
print("You are an seasoned adventurer. You decide to embark on a solo quest through the Python Dungeon....")
print("You arrive at the grand entrance, between you and the door lies a bed of pythons, each one the size of a fully grown man")
print("The distance doesnt look too far to jump...")
companion=0
jump=input("\nWill you take the jump or look for another way around? (Answer Y or N)")
if jump == "Y":
    print("\nYou measure the distance in your head and prepare your run up.\nYou take the leap...")
    print("\n\nYou barely reach the other side of the chasm, the pythons below hiss and spit in anger of missing out on a meal")
    print("\nYou continue onto the 1st level of the dungeon")
    print("\nThe 1st level hold no problems for you as you are stronger than any of the monsters in here.")
    print("You defeat waves of mobs before stumbling across a non hostile goblin who looks to be injured")
    goblin=input("\nDo you help the goblin? (Answer Y or N)")
    if goblin == "Y":
        print("\nYou use your healing magic to seal his wounds...")
        print("\n 'Thank you O Angel!'")
        print("\nHe looks at you, his face is repulsive but his eyes glisten with infatuation")
        print("\n 'I owe you my life. Is there anything I can do to repay you?'")
        goblinFriend = input("\nWill you take the goblin as a companion? (Answer Y or N)")
        if goblinFriend == "Y":
            companion=1
            print("\nYou decide to take the goblin as a companion and head on to the 2nd level of the dungeon...")

        else:
            print("\n 'You repulse me disgusting goblin! I helped you out of pity. Nothing more.'")
            print("\nYou leave the goblin where you found him and proceed to the 2nd level of the dungeon...")

        print("\nSimilar to the 1st floor you have no issues with the mobs on the 2nd level.")
        print("\n\nYou continue on until you reach a weak peasant")
        print("\n Spare any coin for my wares?")
        print("\nYou ponder...The merchant looks frail and weak. (You could easily beat him and steal his wares)")
        merchant=input("\nDo you trade with the merchant or rob him blind (Answer Trade or Steal)")
        if merchant == "Trade":

            print("\nYou give him 100 gold pieces and in return he provides you with a diamond key!")
        else:

            print("\nYou knock the merchant unconscious and rustle through his pockets.")
            print("\nYou find ruby, sapphire and emerald keys")

        print("\n\nYou reach the 3rd floor. There are no mobs here. Just a lone cat dressed as a wizard..")
        print("\nYou have done well to make it this far. Now you must face a riddle.")

        riddle = input("\n  I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
        if riddle == "Echo":
            print("\n....Correct! You may claim your reward but only one item can be taken so choose wisely")
            if merchant == "Trade":
                print("\nYou open the diamond chest and find a minigun inside!")
                print("\nYou take on the dragon without hesitation and basque in a glorious victory!")
                if companion==1:
                    print("\nYou and the goblin take the treasure and go on to adventure together for many more years")
                else:
                    print("\nYou proceed on and claim the treasure. \nYou live for 6 more months until one night you wake to a blade against your throat....\nIts the goblin you left behind in the dungeon...\n\nYOU DIED...")
            else:
                chest=input("\nYou see 3 chests before you, each corresponding with the keys you obtained from the merchant.\n Choose which chest to open")
                if chest == "Ruby":
                    print("\nYou open the chest to find a sword with a ruby blade")
                    print("\nYou take the sword and fight the dragon. It is a difficult battle and you barely make it out alive but you are successful in your quest")
                    if companion==1:
                        print("\nYour companion Goblin fought hard but was lost in battle as you were unable to protect him")
                    else:
                        print("\nYou live to fight another day... until one night you wake to a blade against your throat....\nIts the goblin you left behind in the dungeon...\n\nYOU DIED...")
                elif chest == "Sapphire":
                    print("\nYou open the chest to find a pile of dung...")
                    print("\nYou take the dung and fight the dragon...\n\nYOU DIED...")
                elif chest == "Emerald":
                    print("\nYou open the chest to find a shield made of emerald")
                    print("\nYou take the shield and fight the dragon. You do not manage to slay it but find a secret pathway that leads to the back of the dungeon entrance")
                    if companion==1:
                        print("\nYou managed to protect your goblin companion with the emerald shield. You both live to fight another day")
                    else:
                        print("\nYou live to fight another day... until one night you wake to a blade against your throat....\nIts the goblin you left behind in the dungeon...\n\nYOU DIED...")

        else:
            print("\nIncorrect... You see a bright flash of light and feel intense pain before...Nothing\n\nYOU DIED...")



else:
    print("\nYou decide against the risk of jumping and cautiously take a look around the place before you come across a hidden entrance..")
    print("\nYou enter through the newly found access point to find yourself at the final level of the dungeon!")
    print("\nBefore you have a chance to gather yourself the dragon picks you up in its jaws and bites down hard... \n\nYOU DIED...")


