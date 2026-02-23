#String - Strings in python are surrounded by either single quotation marks, or double quotation .
print("hellow",' ','World')
#Quotes Inside Quotes: You can use quotes inside a string, as long as they don't match the quotes surrounding the string.
print("Hello Guys, today is Asitav's party")
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#Multiline Strings :You can use three double quotes Or three single quotes.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("""========================================================================""")
#Strings are Arrays:strings in Python are arrays of unicode characters,Square brackets can be used to access elements of the string.
a = "Hello World"
print(a[0],a[4],a[5],a[-1])
print("""========================================================================""")
#Looping Through a String:Since strings are arrays, we can loop through the characters in a string, with a for loop.
x = "Bananna"
for x in "Banana":
    print(x)
print("""========================================================================""")
#String Length:To get the length of a string, use the len() function.
x = "Bananna"
print(len(x))
print("""========================================================================""")
#Check String:Check if "free" is present in the following text and  Use it in an if statement:
txt = "Best thing in life is free"
txt1 = "Bestthinginlifeisfree"
print("free" in txt)
print("free" in txt1)

if "free" in txt :
    print("Yes , Free is present")
else:
    print("No Free is not available")

#Check if NOT :
txt = "The best things in life are free!"
print("expensive" not in txt)
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

print("""========================================================================""")
#Slicing:You can return a range of characters by using the slice syntax. 
# Specify the start index and the end index, separated by a colon, to return a part of the string.
j = "The Day is Sunny"
print(j[0:5])

i = "Hello World"
print(i[:7])
print(i[6:])

#Python - Modify Strings : python has set of build in functions .
a = "Myna me is , John !!"
print(a.upper())
print(a.lower())
print(a.strip()) #The strip() method removes any whitespace from the beginning or the end:

#String Concatenation: To concatenate, or combine, two strings you can use the + operator.
a = "Good"
b= "bye"
print(a + b)

#IMP : String Formatting: As we learned in the Python Variables chapter, 
# we cannot combine strings and numbers like this: We need to use F-Strings
'''
age = 36
txt = "My name is asitav, and i am aged" + age
print(txt)
'''


#F-Strings :To specify a string as an f-string, simply put an f in front of the string literal, 
# and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is asitav, and i am aged + {age}"
print(txt)

milk_price = 50
txt = f"milkprice is {milk_price}"
print(txt)
txt1 = f"milkprice is decimal is {milk_price:.2f}"
print(txt1)
print("==============")