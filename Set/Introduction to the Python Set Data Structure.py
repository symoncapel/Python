# A set is a sort of merger of Dictionaries syntax and List syntax

# Uniqueness
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags)

# Nope
#print(tags[0])

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)