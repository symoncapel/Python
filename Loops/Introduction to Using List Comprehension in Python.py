num_list = range(1, 11)
cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)


'''
Coding Exercise
Create a variable called result and use list comprehension to increment each number from the numbers list by 1.
'''

def list_comprehension():
    numbers = [1,2,3,4,5,6]
    result = []
    
    for number in numbers:
        result.append(number + 1)
    
    return result

print(list_comprehension())