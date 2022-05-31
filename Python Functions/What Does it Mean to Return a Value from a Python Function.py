def full_name(first, last):
  return f'{first} {last}'
#print() only shows what it is asked to print where as return actually creates something that can then be stored in a variable such as Kristine. Which can then be used to create a dynamic function. 

Kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')

greeting(Kristine)




'''
Coding Exercise
Create a function called sum_two_numbers that accepts two arguments. The function should 'return' the total of those two arguments added together.
'''
"""
num_one = 4
num_two = 7

def two_numbers(num_one, num_two):
  return num_one + num_two

num = two_numbers(num_one, num_two)

def sum_two_numbers(total):
  print(total)

sum_two_numbers(num)
"""

#This was all they wanted
num_one = 4
num_two = 7
def sum_two_numbers(num_one, num_two):
  return num_one + num_two