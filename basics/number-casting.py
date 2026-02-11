#Numbers : int/float/complex
#int example
a = 20 
a1 = int(20)
b = -30.30
b1 = int(-30.30)
c = 20.324
c1 = int(20.324)
print(a,b,c)
print(a1,b1,c1)

#float - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.10

x1 = 12E4
y1 = 12E4
z1 = -87.7e100

print(x,y,z,x1,y1,z1)

#Complex - Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#int() - constructs an integer number from an integer literal, 
# a float literal (by removing all decimals), or a string literal .
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

#Casting 
#Create a variable x with the integer value 1
x =1
#Convert x to a float and store it in a
a = float(x)
#Convert x to a string and store it in b
b = str(x)
#Print a, b, and their types
print(x,' ',a,'',b)
print(type(x))
print(type(a))
print(type(b))



