'''
def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())

# it is considered a very bad practice to ever set a default argument as a list.
'''


'''
Coding Exercise
Create a function called counter that accepts an argument called initial_count and returns that argument incremented by 1. initial_count must have a default value of 0.
'''

def counter(initial_count=0):
  return initial_count + 1
print(counter(initial_count=0))