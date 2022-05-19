usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

#continue = continue through the loop
'''
for username in usernames:
    if username == 'cersei':
        print(f"Sorry, {username} you are not allowed")
        continue
    else:
        print(f"Welcome back {username}")
'''

#break = stops after what you asked it to find
'''
for username in usernames:
    if username == "cersei":
        print(f"{username} was found at index {usernames.index(username)}")
        break
    print(username)
'''


#Coding Exercise
#Write a loop that loops over the list of vegetables and prints each one out. When it reaches 'apple' it should print 'apple is not a vegetable' and then break.

def loop_and_break():
    vegetables = ["onion", "broccoli", "apple", "spinach"]
    
    for fruit in vegetables:
        if fruit == "apple":
            print(f"{fruit} is not a vegetable")
            break
        print(fruit)

loop_and_break()