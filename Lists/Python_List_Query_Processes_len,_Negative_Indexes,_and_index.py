
tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags) #how we could get a count of all of the elements in the list.
last_item = tags [-1]      #how you get the value from the last item even if you don't know what its index was. using a negative index.
index_of_last_item = tags.index(last_item) #how once you do have the value for one of your elements you can pass it to the index function right here and then it will go traverse through the entire list and return the index of that value.


print(last_item)
print(number_of_tags)
print(index_of_last_item)