'''
legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)
'''

'''
def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    result.append(numbers + 1) #keep it simple
    print(result)

    return result
loop_over_list()
'''


def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []

    for number in numbers:
        result.append(number+1)
    
    return result