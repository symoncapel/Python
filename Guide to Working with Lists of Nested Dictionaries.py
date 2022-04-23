teams = [ # [] = a list
    {
        'astros': {
            '2B': 'Altuva',
            'SS': 'Correa',
            '3B': 'Bregman',
        }
    },
    {
        'angels': {
            'OF': 'Trout',
            'DH': 'Pojols',
        }
    }
]

#print(teams[0])
#{'astros': {'2B': 'Altuva', 'SS': 'Correa', '3B': 'Bregman'}}

# {} = a dictionary
# 'astros' = key
# {'2B': 'Altuva', 'SS': 'Correa', '3B': 'Bregman'} = nested dictionary/value

#angels = teams[1].get('angels', 'team not found')
#print(angels)
# {'OF': 'Trout', 'DH': 'Pojols'}

angels = teams[1].get('angels', 'team not found')
print(list(angels.values())[1])
# Pojols


#angels = teams[1].get('angels', 'team not found')
#print(list(angels.values())[1]) 
#
# teams[1] treats it like a list (should show you if it a dictionary)
# .get() returns the value of the item with the specified key. ('angels') this iis the key that we want
# 
# .values() = we called get on it and we said this is the key that we want and then from there we were able to grab all of those values.
# .list() = Turn it into a dictionary view object convert that into a list and then we were able to treat that as a plain old python list
# [] = grab any of the elements we want.
# 
