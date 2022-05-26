# List of comparison operators
# == Equality  
# != Inequality
# <> Inequality (deprecated) SHOULD NOT EVER USE BECAUSE IT IS OUTDATED!
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

#strings can only use
    # == Equality  
    # != Inequality

#int can use
    # == Equality  
    # != Inequality
    # >  Greater than
    # >= Greater than or equal to
    # < Less than
    # <= Less than or equal to

'''
username = 'jonsnow'

if username == 'jonsnow':
  print('Welcome Jon')
else:
  print('You shall not pass!')


age = 25

if age <= 25:
  print(f"I'm sorry, you need to be at least 25 years old")
'''

user_list = ['symon', 'jackson', 'jeff', 'Diana']
other_list = ['jeff', 'Diana']

if user_list >= other_list:
  print('they match')