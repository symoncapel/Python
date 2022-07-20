
'''
__init__

double underscores in front of the name, how python works with private and protected methods inside of their classes 
'''



#Dunder string

class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total


    def __str__(self):                                                #used for debugging
        return f"Invoice from {self.client} for {self.total}"

inv = Invoice('Google', 500)
print(str(inv))