friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
print(friends)
print(len(friends))
random_card = random.randint (0, len(friends)-1)
if random_card == 0:
    name = (friends[0])
    print (friends[0])
elif random_card == 1:
    print(friends[1] + " will pay the bill")
elif random_card == 2:
    print((friends[2]) + " will pay the bill")
elif random_card == 3:
    print((friends[3]) + " will pay the bill")
elif random_card == 4:
    print((friends[4]) + " will pay the bill")

#you can also use random.choice to randomly generate an item from a list
print(random.choice(friends) + " will pay the bill")
#you can also use random.randint to the same effect
print(firends[random.randint] + " will pay the bill")
