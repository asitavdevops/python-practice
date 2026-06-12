# Randomization & python lists
# Create random number between 0 and 20 using ramdom module (https://docs.python.org/3/library/random.html)
#import random
random_integer = random.randint(0, 20)
print(random_integer)

random.random() - Return the next random floating-point number in the range 0.0 <= X < 1.0
random.uniform(a, b)-Return a random floating-point number N such that a <= N <= b 
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)

# Coin flip program for Heads and Tails 
random_heads_tails = random.randint(0, 1)
print(random_heads_tails)

if random_heads_tails == 0:
    print("Heads ")
else:
    print("Tails ")

#List - ordered collection of items, can be of any data type, mutable (can be changed after creation), allows duplicate values
#fruits = [item1, item2 ,item3]

#display states of united states who joined first :
usa_states_by_admission = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
    "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

print(usa_states_by_admission[0])
print(usa_states_by_admission[-2])

#Change/subsitute item in list
usa_states_by_admission[-1] = "HAWAIL"
print(usa_states_by_admission[-1] )

#adding item to the list end 
usa_states_by_admission.append("AsitavLand")
print(usa_states_by_admission)

#adding multiple items to the list end 
usa_states_by_admission.extend(["AmitavLand" , "SupriyaLand"])
print(usa_states_by_admission)

#Code - Who will pay the Bill
#solution 1:
import random
friends = ["Charli", "Bob", "Allice", "Katty", "Asitav", "Ravi"]
WPB = random.choice(friends)
print(f"Bill on :{WPB}")
#solution 2:
random_index = random.randint(0, 5)
print(f"2 solution who will pay the bill: {friends[random_index]}")

#Index error(list index out of range) && Nested list:
test = ["Charli", "Bob", "Allice", "Katty", "Asitav", "Ravi"]
print(f"length of the test index is :{len(test)} : {test[5]}")

#Nested list example .#1. All food items whaich are using pestisides 
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Grapes", "Peaches", "Pears", "Nectarines", "Apples", "Peppers", "Cherries", "Blueberries", "Green Beans"]

#segrigate vegitale and Fruits 
fruits = ["Strawberries", "Grapes", "Peaches", "Pears", "Nectarines", "Apples", "Cherries", "Blueberries"]
vegetables = ["Spinach", "Kale, Collard & Mustard Greens", "Bell & Hot Peppers", "Green Beans"]

# #now use nested list for above one example
dirty_dozen_nested_list = [ fruits, vegetables ]
print(dirty_dozen_nested_list)

"""
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

"""

#Project Rock Paper Scissors for Schools
import random
# ASCII Art representations for the game choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_input = int(input("What do you choose ? Type 0 for Rock, 1 for Peper or 2 for scissors \n"))

if user_input == 0:
    print(f"You choose rock :{rock}")
elif user_input == 1:
    print(f"You choose paper : {paper}")
elif user_input == 2:
    print(f"You choose scissors : {scissors}")
else:
    print("Provide input from 0-2")
    exit ()

sys_random_input = [ rock, paper , scissors ]
random_input = random.choice(sys_random_input)
print(f"computer choose :{random_input}")

if user_input == random_input:
    print("You Win !!! Congratulation")
else:
    print("You loose !! Try again")


