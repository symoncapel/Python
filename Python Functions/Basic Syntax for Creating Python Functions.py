'''
def full_name(first, last):
    print(f"{first} {last}")

full_name('Symon', 'Capel')
'''
'''
def auth(email, password):
    if email == 'symon@gmail.com' and password =='secret':
        print("Authorized")
    else:
        print("Not autherized")

auth('symon@gmail.com', 'secret')
'''

def hundred(max_value):
    for num in range (1, max_value):
        print(num)
hundred(401)