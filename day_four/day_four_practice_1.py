# randomisation // random module
# importing the random madule so we can generate random numbers
import random

# importing my_module file so we can use the code inside of it
import my_module

print(my_module.favorite_number)

random_number= random.randint(1, 10)
# int random number
print(random_number)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)
# getting a random floting point number between 0 to 1 and multiplying it by 10, so that it generate a floating point number between 0 to 10


random_float = random.uniform(5, 15)
print(random_float)




# heads or tails practice using random 
heads_or_tails = random.randint(0, 1)
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")




# who pay