#Python Dictionaries
"""
Python is a data structure that stores data in key-value pairs.
Example:
| Key (Word) | Value (Meaning) |
| ---------- | --------------- |
| `"name"`   | `"Asitav"`      |
| `"age"`    | `25`            |
| `"city"`   | `"Bangalore"`   |

Syntax: {Key: Value}
A dictionary is created using curly braces {}
Key - kind of column 
Value - value for that column
"""
#Example:
program_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected",
    "Function": "A pice of coad that you can easily call over and Over",
    "Loops": "The action of doing sonthing over and Over again"
}
#Retrive the dictionary
print(program_dictionary["Function"])
#how to add new key to the dictionary
program_dictionary["ph_number"] = "9880386544"
print(program_dictionary)

#Create Empty Dictionary
empty_dictionary = {}
empty_dictionary[123] = 112233
print(empty_dictionary)

#Wipe a dictionary
# program_dictionary = {}
# print(f"Now the program dictionart is empty : {program_dictionary}")

#Edit an item in a dictionary
print(program_dictionary["Bug"])
program_dictionary["Bug"] = "A mark in your laptop."
print(program_dictionary)

#Loop throught a dictionary 
for key in program_dictionary:
    print(key)
    print(program_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for student in student_scores:
    score = student_scores[student]
    
    if score > 90 :
        student_grades[student] = "Outstanding"
    if score > 80 and score <= 90 :
        student_grades[student] = "Exceeds Expectations"
    if score > 70 and score <=80 :
        student_grades[student] = "Acceptable"
    if score <= 70 :
        student_grades[student] = "Fail"
    
print(student_grades)

# Nesting :
"""
{
    key: [List],
    key2: {Dictionary},
}
"""
#Nested list in dictionary 
"""
Cant be put multiple value for a key in dictionary but can be used list
travel_log = "Mumbai","Delhi","Kanpur"
Note: the above senario cant be possible 
"""
#Now use Nested list in dictionary 
travel_log = {
    "India": ["Mumbai","Delhi","Bhubaneswer"],
    "usa": ["New Jersy","Macao","Texas"]

} 

print(travel_log["India"][1])

#Nested list
nested_list = ["A","B",["C","D"]]
print(nested_list[2][0])

#Nested Dictionary:
travel_log = {
    "India": {
        "City_visited": ["Mumbai","Delhi","Bhubaneswer"],
        "total_visits": 6 ,
        
    },
    "usa": {
        "City_visited": ["New Jersy","Macao","Texas"],
        "total_visits": 5 ,
        
    }

} 

print(travel_log["usa"]["City_visited"][2])