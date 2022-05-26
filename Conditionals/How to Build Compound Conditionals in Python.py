'''
username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')
'''

'''
logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')
'''



'''
Coding Exercise
Fill in the below conditional with a compound condition that will print "Success!" if "number" is anything between 1 and 100 (inclusive).
'''


number = 1
def compound_conditional(number):
    
    if number >= 1 and number <= 100:
        print("Success!")
    else:
        print("Failure...")
compound_conditional(number)