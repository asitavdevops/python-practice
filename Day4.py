# Randomization & python lists
# Create random number between 0 and 20 using ramdom module (https://docs.python.org/3/library/random.html)
import random
# random_integer = random.randint(0, 20)
# print(random_integer)

#random.random() - Return the next random floating-point number in the range 0.0 <= X < 1.0
#random.uniform(a, b)-Return a random floating-point number N such that a <= N <= b 
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

# Coin flip program for Heads and Tails 
random_heads_tails = random.randint(0, 1)
print(random_heads_tails)

if random_heads_tails == 0:
    print("Heads ")
else:
    print("Tails ")