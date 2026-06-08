#check the variable data type
print(type("Hellow"))
a=True
b=13.50
c=123,345,23
print(type(a),type(b),type(c))

#Mathematical Operations (PEMDAS - LeftoRight)
print(3 * 3 + 3 / 3 -3)
print(3 * (3 + 3) / 3 -3)

#Assignment Operator [+= -= *= /= ]
score = 0
score = score + 1
print(score)
score +=1
print(score)
score -=1
print(score)

# f-strings
score = 0
height = 5.8
is_winning = True
print(f"your score is :{score},Your Height is :{height},Are you winning:{is_winning}")
