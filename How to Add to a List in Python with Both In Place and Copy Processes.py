tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming'

# In Place
tags.extend('Programming')
tags.extend(['Programming'])

# New List
new_tags = tags + ['Programming'] #Best Practice

print(new_tags)

print(tags)