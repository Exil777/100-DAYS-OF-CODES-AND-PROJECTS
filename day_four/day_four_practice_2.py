# guess who pay the bills
import random

friends = ["Jake", "Charles", "Jameson", "James", "Peter"]

random_friend = random.choice(friends)
print(random_friend)


# the other other option is to find the random friend is
random_number = random.randint(0, 4)
random_index = friends[random_number]
print(random_index)
