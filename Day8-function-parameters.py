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
#Hints:
#index() inbuild function can be used here 
#fruits["apple", "Orange","grape"] -->fruits.index("orange") = 1

#Coading Project Caesar Cipher .
#Todo 1- import the logo
import art
print(art.logo)
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


"""
#TODO 1- create a function called encrypt() that takes original text  and shift number as 2 inputs.
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabets.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabets) #Handling when if you forward from z by 9 place (IndexError: list index out of range)
        #shifted_position %= len(alphabets)
        cipher_text = cipher_text + alphabets[shifted_position]
        #Cipher_text += alphabets[shifted_position]
    
    print(f"Here is the Encrypted result : {cipher_text}")
"""


"""
#encrypt(original_text=text ,shift_amount=shift) 
def decrypt(original_text, shift_amount):
    output_text = ""

    for letter in original_text:
        shifted_position = alphabets.index(letter) - shift_amount
        shifted_position = shifted_position % len(alphabets) #Handling when if you forward from z by 9 place (IndexError: list index out of range)
        #shifted_position %= len(alphabets)
        output_text = output_text + alphabets[shifted_position]
        #Cipher_text += alphabets[shifted_position]
    
    print(f"Here is the Encrypted result : {output_text}")

"""


#Now use create a final function call ceasar and integrate both encrypt & decrypt function in it 
def Caesar(original_text, shift_amount, encrypt_or_decrypt):
    output_text = ""
    if encrypt_or_decrypt == "encode":
               shift_amount *= -1
    for letter in original_text:
        #Todo 2- If user input number/Symbols/spaces
        if letter not in alphabets:
            output_text += letter
        else:
            
               shifted_position = alphabets.index(letter) + shift_amount
               shifted_position = shifted_position % len(alphabets) #Handling when if you forward from z by 9 place (IndexError: list index out of range)
        #shifted_position %= len(alphabets)
               output_text = output_text + alphabets[shifted_position]
        #Cipher_text += alphabets[shifted_position]
    
    print(f"Here is the {encrypt_or_decrypt}d result : {output_text}")

    

#Restart the Cipher program .
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt \n").lower()
    text = input("provide your message: \n").lower()
    shift =int(input("Type the shift number: \n"))
    
    Caesar(original_text=text, shift_amount=shift ,encrypt_or_decrypt=direction)

    restart = input("Type 'Yes' if youwant to continue . Otherwise type 'No' .\n").lower()
    if restart == "no":
        should_continue == False
        print("GoodBye !!!")











        

     

