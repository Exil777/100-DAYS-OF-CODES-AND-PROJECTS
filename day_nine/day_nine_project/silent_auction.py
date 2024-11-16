# TODO-1: Ask the user for input
print("Welcome to the Silent Auction game.")
# name = input("What is your name? ")
# price = int(input("What's your price? "))
# TODO-2: Save data into dictionary {name: price}
# bids[name] = price

# TODO-4: Compare bids in dictionary
def find_hightest_bidder(bibbing_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bibbing_dictionary:
        bid_amount = bibbing_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

# TODO-3: Whether if new bids need to be added
bids = {}
continue_bids = True
while continue_bids:
    name = input("What is your name? ")
    price = int(input("What's your price? "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        continue_bids = False
        find_hightest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 30)


