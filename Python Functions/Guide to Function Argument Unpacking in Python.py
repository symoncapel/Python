def greeting(*args): # *=unpacked args=arguments
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')