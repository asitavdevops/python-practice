#Printing :

# print('Hello world !') #python '' or "" is also used for defining strings

#Strings Manipulation :
# print("Hello world\nHello World\n Hello World") #\n is used for new line)
# print("Hello" + " Asitav" + "\nHello" + "  Amitav") # + is used for concatenation of strings

#input function from user :
# print("Hello - " + input("Enter user name :") + " !")
# age = input("Enter you age :")
# print("You are :" + age + " Years old !")

# ch_count = input("Enter a string :")
# print("Length of the string" + ":" + str(len(ch_count)))

# length=len(input("Provide a string : "))
# print(length)

#3 lines of code to switch the contents of the variables
# var1 = input("Enter variable 1 :")
# var2 = input("Enter variable 2 :")
# var3 = var1
# var1 = var2
# var2 = var3
# print("now the variable 1 is :" + var1)
# print("Now variable 2 is :" + var2)

#Project: Band Name Generator
GREEN = "\033[92m"
RESET = "\033[0m"

print(f"{GREEN}Click Run to run the final project you will build{RESET}")
city=input("What is the name of the city you Grow up in :\n")
pet_name=input("What's your Pet name :\n")
print("Your band name could be :" + city + " " + pet_name)