users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users] #not a good idea, see below.

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)


# whenever you have more than one data type inside of a list it means you're going to have to be very careful with how you treat that list. Typically I 
# try to keep my list as straightforward as possible so I try to keep the exact same data type in there. So that means that if I have a list of other 
# lists then I only want to have a collection of lists that would look something like this.
#nested_list = [[123], [234], [456]]