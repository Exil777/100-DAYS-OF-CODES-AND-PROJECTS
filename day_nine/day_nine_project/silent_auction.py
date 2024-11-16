# TODO-1: Ask the user for input
print("Welcome to the Silent Auction game.")
# name = input("What is your name? ")
# price = int(input("What's your price? "))
# TODO-2: Save data into dictionary {name: price}
bids = {}
# bids[name] = price
# TODO-3: Whether if new bids need to be added
continue_bids = True
while continue_bids:
    name = input("What is your name? ")
    price = int(input("What's your price? "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        continue_bids = False
# TODO-4: Compare bids in dictionary
