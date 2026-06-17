#Create function greet(),3 print inside function and call the function
# def greet():
#     print("Hello Asitav")
#     print("This is function behaviour in python : Asitav")
#     print("How is the weather: Asitav")

# greet()

#Functions with inputs:
"""
def my_fun(Somthing):
    do this 
    do that 
    Finally do this 

#Functions with inputs examples :
def greet_name(name):
    print(f"Hello :{name}")
    print(f"This is function behaviour in python : {name}")
    print(f"How is the weather: {name}")

greet_name('Asitav')
greet_name('Supriya')

#note- in the above function "name" is called as parameter and arguments passed during function calling .

"""

"""
#Functions with more then 1 inputs:
def greet_with(name,location):
    print(f"Hello - {name}")
    print(f"What is it like {location}")

greet_with("Asitav","Bangalore")
#positional Argument - if we interchange the value then what happen to function
greet_with("Bangalore","Asitav")

"""

"""
#function keyword Arguments :
# def my_fun(a , b , c):
#     do this with a 
#     do that with b
#     Finally do this with c
# my_fun(a=2, b=4, c=9)

#Example of Keyword parameters and Arguments in function:
def greet_with(name,location):
    print(f"Hello - {name}")
    print(f"What is it like {location}")

greet_with(name="Abhisek Viramalla", location="Chennai")

#note : Here reet_with(name,location): - name and location are two parameters
#       and print(f"Hello - {name}") - {name} - is the argument to the parameter in the function.
"""
#Love Calculator:
"""
print("Welcome to Love Calculator !!")
def calculate_love_score(name1,name2):
    combined_name = name1 + name2
    lower_combined_name =combined_name.lower()
    print(lower_combined_name)
    #true love calculate now
    t = lower_combined_name.count("t")
    r = lower_combined_name.count("r")
    u = lower_combined_name.count("u")
    e = lower_combined_name.count("e")
    
    first_true_val = t + r + u + e
    # print(t,r,u,e)
    # print(first_true_val)

    l = lower_combined_name.count("l")
    o = lower_combined_name.count("o")
    v = lower_combined_name.count("v")
    e = lower_combined_name.count("e")

    second_love_val = l + 0 + v + e
    #print(second_love_val)

    print(f"Love percentage for both of you is :{str(first_true_val) + str(second_love_val)}")


calculate_love_score("Asitav Pattanaik","Supriya Singh")

"""

#Coading Caesar Cipher
encode_decode_user_input = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n")
msg = input("Type your message : \n")
shift_number = input("Type your shift number :\n")
print("Here is the encoded result : ")
user_input_yes_no = input("Type 'yes' if you want to go again . Otherwise type 'no' \n")
user_input = ("Type 'encode' to encrypt , type 'decode' to decrypt: \n ")
msg2 = input("Type your message :\n")
shift_number2 = input("Type your shift number :\n")
