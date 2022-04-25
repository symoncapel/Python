from functools import reduce

"""
manual_exponent(2, 3)
"""

def manual_exponent(base_num, pow_num):
    result = 1
    for index in range(pow_num):
      result = result * base_num
    return result

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))


# iterative solution
def manual_exponent(num, exp):
    counter = exp -1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))


#functional solution
def manual_exponent(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list))

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))