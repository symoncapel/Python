"""
User Database Query
Kristine
Tiffany
Jordan
"""
#create a list
users = ['Kristine', 'Tiffany', 'Jordan']
print(users)

#Adding to the list by location in the list
users.insert(0, 'Anthony')
print(users)

#simply adding to the list
users.append('Ian')
print(users)

#search or quary the list and return with a string
print(users[2])

##search or quary the list and return with its own list
print([users[2]])

#How to replace and reaisign in a list
users[4] = 'Braydon'
print(users)