'''
M3C5 Python Assignment

During this section of Module 3, you have learned more about Python. Python is a powerful programming language that serves a lot of purposes. To practice what you have learned in this section, you will complete some Python exercises. You may use Visual Studio Code, Repl.it, or another text editor/environment of your choice. Please complete the following assignment and reach out on the Support App to have a mentor review your work. If you have any questions or need any help, please reach out so we can help you! This assignment must be completed to pass this section of the coursework.

Exercise 1: 
Create a dictionary called student with the keys: name, age, major, year, and classes.
Exercise 2:
Use the get method to print the value of the key “name”.
Exercise 3:
Use the pop method to remove “year” from the dictionary.
Exercise 4:
Add the key/value pair of “gpa” : 3.9 to the dictionary.
Exercise 5:
Change the “gpa” value from 3.9 to 4.0
Exercise 6:
Create a new dictionary with the name collegeStudents and make it so the keys are name, age, major, year, and gpa. The values are in a list, where each index in the list is a student. Next, add a few students.
Exercise 7:
Sort the dictionary
'''



'''
from unicodedata import name
from webbrowser import get


student = {
    "name": "Symon",
    "age": 33,
    "major": "Engineer",
    "year": "2022",
    "classes": "4"
}
print(student)

name = student.get("name")

remove_year = student.pop("year")

student.update(gpa = 3.9)

student.update(gpa = 4.0)
'''

collegeStudent = {
    "name": ["Charlie", "Tommy", "Angie", "James"],
    "age": ["33"],
    "major": ["Engineer"],
    "year": ["2022"],
    "gpa": [4.0]
}

collegeStudent ["name"] += ["Diana", "Jackie"]

'''
sorted_keys = collegeStudent.items()
new_items = sorted(sorted_keys)
print(new_items)
'''

for value in sorted(collegeStudent.items(), key=lambda x: x[0], reverse=False):


    sorted(collegeStudent.keys())
for key in sorted(collegeStudent.keys()) :
    print(key , " : " , collegeStudent[key])

'''
my_result = dict()
for key in sorted(collegeStudent):
   my_result[key] = sorted(collegeStudent[key])

print(my_result)
'''