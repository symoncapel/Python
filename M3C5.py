

from unicodedata import name
from webbrowser import get


student = {
    "name": "Symon",
    "age": 33,
    "major": "Full-Stack Dev",
    "year": 2022,
    "classes": 5,
}

name = student.get(student(name))

print(name)

remove_year = student.pop("year")

student.update("gpa": = "3.9")

student.update("gpa": = 4.0)