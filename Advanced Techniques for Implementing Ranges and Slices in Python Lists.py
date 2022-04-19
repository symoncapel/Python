tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[::2]
#grabs every other element
print(tag_range)
#['python', 'tutorials', 'programming']

tag_range = tags[::-1]
#reverses the ranges by elements
print(tag_range)
#['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

tags.sort(reverse=True) 
#sorts the elements alphabetically and then prints them
#  in reverse order.
print(tags)
#['tutorials', 'python', 'programming', 'development', 'computer science', 'code']

sorted_tags = tags.sort(reverse=True)
print(sorted_tags)
#None (THE KEY: the sort function changes tags but it doesnt store it as a standard opperation inside a variable)
