import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

# to find a median all numbers must be in order smallest to largest and then find the number in the middle of the set of numbers.

in_order = sorted(sale_prices)
print(in_order[4:5])

#tag_range = in_order[4:5]
#print(tag_range)


sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
median = sorted_list[math.floor(num_of_sales/2):(math.floor (num_of_sales/2) + 1)]

print(median)





#Show notes
'''
#import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)
'''