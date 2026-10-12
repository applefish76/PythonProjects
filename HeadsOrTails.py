# this is a random heads/tails generator with a 50% chance of either result

random_heads_or_tails = random.randint (0,1)
if random_heads_or_tails == 0:
    print("tails")
else:
    print("heads")

# if we wanted to fix this game to be more likely to hit heads.
fixed_heads_or_tails = random.randint (0,10)
if fixed_heads_or_tails <= 3:
    print("tails")
else:
    print("heads")
# this means whenever the random int generates 3 or lower, then it will land on tails. Anything above 3 would land on heads


