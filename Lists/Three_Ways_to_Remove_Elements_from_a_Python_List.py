users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']
print(users)


#Removes list item
users.remove('Jordan')
print(users)
#If you are working with a list where you know the value, then this remove function and passing in that value is typically the way to go. This makes it possible to simply search through the entire collection and then remove any element that matches this value.


popped_users = users.pop()
print(popped_users)
# pop this is what you're typically going to use when you want the very last element in the list and you want to use that you want to pop it off the stack and use it in your program.


del users[0]
print(users)
# this is what you would use when you know the list. And you know the index value for the list.