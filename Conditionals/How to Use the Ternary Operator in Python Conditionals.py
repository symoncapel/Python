role = 'admin'

auth = 'access granted' if role == 'admin' else "access denied" #should be readable almost like a sentance

#Traditional ternary syntax
if role == 'admin':
    auth = 'access granted'
else:
    auth = "access denied"
print(auth)



'''Coding Exercise
Write a ternary operator that sets "language_check" to True if "language" is set as "python", and sets it to False if it's not.'''

language = "python"

language_check = True if language == "python" else False  #should be readable almost like a sentance
print(language_check)