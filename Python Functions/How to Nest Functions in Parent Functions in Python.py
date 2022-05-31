"""
def greeting(first, last):
    def full_name():
        return f'{first} {last}'


    print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')
"""




"""
Coding Exercise
Create a function called greeting that accepts a persons name as an argument. Your function should return "Hello, {persons name}".

Example: Passing in 'Jordan' should return 'Hello, Jordan'
"""

def greeting(first_name):
    def persons_name():
        return f'{first_name}'

    print(f'Hello, {persons_name()}')


greeting('Symon')



def greeting(name):
    greeting = f'Hello, {name}'
    return greeting
greeting('Symon')