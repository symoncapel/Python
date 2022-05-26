'''
list = ['stuff', 'desk', 'hat', 'charger', 'other_stuff']
print(list[1:-1])
'''

def remove_first_and_last(list_to_clean):
    _, *content, _ = list_to_clean
    return content

list = ['stuff', 'desk', 'hat', 'charger', 'other_stuff']
print(remove_first_and_last(list))