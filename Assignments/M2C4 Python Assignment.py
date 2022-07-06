#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

list = ['apple', 'strawberry', 'kiwi']
print(list)

tuple = ('horse', 'dog', 'chicken',)
print(tuple)

num = float(6.8)
print(num)

whole_num = int('4')
print(whole_num)

decimal = .3
print(decimal)

ranch = {
    'barn': ['red', 'tack room', 'animals'],
    'tractor': 'green',
    'silo': 'grain storage',
}
print(ranch)


#Exercise 2: Round your float up.
round_num = round(num)
print(round_num)


#Exercise 3: Get the square root of your float.
import math
square_num = math.sqrt(num)
print(square_num)


#Exercise 4: Select the first element from your dictionary.
barn = ranch['barn']
print(barn)


#Exercise 5: Select the second element from your tuple
print(tuple[1])


#Exercise 6: Add an element to the end of your list.
new_list = list + ['watermelon']
print(new_list)


#Exercise 7: Replace the first element in your list.
list[0] = 'orange'
print(list)


#Exercise 8: Sort your list alphabetically.
print(sorted(list))


#Exercise 9: Use reassignment to add an element to your tuple.
tuple += ('cat',)
print(tuple)