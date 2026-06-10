#If else condition && Operatore [> < >= <= == !=]
"""
if condition:
    do this
else:
    do this
"""

# print("Welcome to Roller costar ride !!")
hg = int(input("Enter your hight in CM :"))

if hg >= 120:
    print("Congrats you can take the ride!!")
else:
    print("You cant enter the ride !! Sorry")   

modulo operator:
print(f"{10%2},{10%3}")

Find Even or odd number
Num = int(input("Enter a Number !! :\n"))
if Num % 2 == 0:
    print("Its a Even Number")
else:
    print("Its a Odd Number")

#Nested if else condition:
"""
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
========Another Way=====================
    if condition1:
        do A
    elif condition2:
        do B
else:
    do C
"""
#Solve https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D
print("Welcome to Roller costar ride !!!")
hg = int(input("Enter your height in CM : \n"))
age = int(input("Enter you age !! \n"))

if hg >= 120:
    print("Great, you are eligible for ride")
    if age < 12:
        print("Pay $5 for the ride")
    elif age > 18:
        print("Pay $12 for the ride")
    else:
        print("Pay $7")

else:
    print("Hight below 120 CM are not eligible for a ride")

"""
Multiple If: If all 3 conditions True then A,B,C will be executed
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
"""
#Solve https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D
print("Welcome to Roller costar ride !!!")
hg = int(input("Enter your height in CM : \n"))
bill = 0
if hg >= 120:
    print("Great, you are eligible for ride")
    age = int(input("Enter your Age : "))
    if age <= 12:
        print("Child ticket is $5")
        bill = 5
    elif age >= 18:
        print("Adult ticket is 12$")
        bill = 12
    else:
        print("youth Ticket is 7$")
        bill = 7

    want_photo = input("Want to take photo ? type yes or no :")
    if want_photo == "yes":
        #bill = bill + 3
        bill += 3
    print(f"Your Bill is ${bill}")

else:
    print("Hight below 120 CM are not eligible for a ride")

#Pizza Order Program :
print("Welcome to Python Pizza Delivery")
size = input("What size pizza you want ? S, M or L :")
cron = input("Do you want corn in your pizza ? Y or N  :")
extra_cheese = input("Do you want extra cheese ? Y or N :")

bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
small_pizza_corn = 2
l_m_pizza_corn = 5
extra_c = 1

if size == "S":
    bill = small_pizza
elif size == "M":
    bill = medium_pizza
elif size == "L":
    bill = large_pizza

else:
    print("You have wrong input .")

if cron == "Y":
    if size ==  "S":
        bill += small_pizza_corn
    else:
        bill += l_m_pizza_corn

if extra_cheese == "Y":
    bill += extra_c
    
    
print(f"Total bill you pay ${bill}")

Logical Operator :
"""
if condition1 & condition2 & condition3:
    do A
else:
    do B
"""
