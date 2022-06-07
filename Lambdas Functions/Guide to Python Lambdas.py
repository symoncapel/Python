'''
full_name = lambda first, last: f'{first} {last}'


def greeting(name):
    print(f'Hi there {name}')


greeting(full_name('Symon', 'Capel'))
'''




'''
Coding Exercise
In the code below, create a variable called "greeting" and assign it a lambda function that accepts a name as an argument, and return the string "Hi, name".

Example: If you pass in the name "Jordan", it should return "Hi, Jordan".
'''
'''
greeting = lambda name: f'{name}'


def lambda_practice(name):
    print(f'Hi, {name}')

    return greeting
    

lambda_practice(greeting('Symon'))
'''

'''
def lambda_practice(#name):
    greeting = lambda name: f'Hi {name}'
    
    return greeting('Symon')
    
#print(lambda_practice()) #don't need this
'''

def lambda_practice():
    greeting = lambda name: f'Hi, {name}'

    return greeting