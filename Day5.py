"""
#Pythin Loops : 
for item in list_of_items:
    #Do somthing to each item 
"""

"""
#Example:
fruits = [ "Apple" , "Peach" , "Pear" ]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    #print(fruits)
print(fruits)

"""


"""
# for Multiple student numer list . Add the total number and provide the Max number 
student_marks = [34, 41, 47, 53, 59, 64, 71, 78, 86, 95]
sum_student_marks = sum(student_marks)
print(sum_student_marks)

#same this for loop:
sum = 0
for mark in student_marks:
    sum = sum + mark
print(f"students final mark :{sum}")

#Find the max number in the list
print(f"Max number from the student_marks is without for loop : {max(student_marks)}")

max_number = 0
for number in student_marks:
    if number > max_number:
        max_number = number
print(f"for loop using max number is :{max_number}")

"""

#For loop with range() function:
"""
for number in range(a, b)
    print(number)
"""

"""
#Example:
for number in range( 1, 11 ):
    print(number)

for number in range( 1, 11, 3):
    print(number)

"""

"""
#Code to sum from 1 to 100
final_val = 0
for number in range( 1, 101 ):
    final_val += number
print(f"sum of number from 1 to 100: {final_val}")

"""
"""
#Project : Python password Generator :
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
    ',', '.', '<', '>', '?', '/', '|', '\\'
]

print("Welcome to python password Generator !")
input_letters = int(input("How many letters would you like in your password : \n"))
input_words = int(input("How many words would you like in your password : \n"))
input_symbols = int(input("How many symbols would you like in your password : \n"))

#Simple Way coading 
# password = ""

# for char in range( 1, input_letters + 1):
#     random_letter = random.choice(letters)
#     password = password + random_letter
    
# for word in range( 0, input_words ):
#     password += random.choice(numbers)
    
# for symbol in range( 0, input_symbols ):
#     password += random.choice(symbols)

# print(f"Here is your password: {password}")

#Hard way of coading :
password = []

for char in range( 0, input_letters ):
    password.append(random.choice(letters))
for word in range( 0, input_words ):
    password.append(random.choice(numbers))
for sym in range( 0, input_symbols ):
    password.append(random.choice(symbols))

#print(password)

random.shuffle(password)
#print(password)

final_pwd = ""
for char in password:
    final_pwd += char
print(f"code Generated password recomendation to use : \n {final_pwd}")


"""


