
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def highest_bidder():
    highest_bid = 0
    winner_name = ""
    for person, bid in bids_dict.items():
        if int(bid) > int(highest_bid):
            highest_bid = bid
            winner_name = person
    print(f"The winner is {winner_name} with a bid of £{highest_bid}!")

print(logo)
print("Welcome to the blind bid")

bids_dict = {}

name = input("What is your name?\n").lower()
bid = input("What is your bid?\n")
bids_dict[name] = bid

no_more_bids = False
while no_more_bids == False:
    print("\n" * 100)
    more_bids = input("Are there any more bids?\n").lower()
    if more_bids == "yes":
        name = input("What is your name?\n").lower()
        bid = input("What is your bid?\n")
        bids_dict[name] = bid
    else:
        no_more_bids = True
        print("\n" * 100)
        highest_bidder()
















