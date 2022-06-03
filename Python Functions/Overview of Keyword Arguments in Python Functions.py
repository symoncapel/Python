def greeting(**kwargs): # **=
  print(kwargs)
# a keyword argument needs to have a set of keys and associated values which as you know is the very definition of a dictionary and so that is one of the key elements to remember.

greeting()
greeting(first = 'Kristine', last = 'Hudgens')



def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens')