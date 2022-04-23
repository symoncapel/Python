post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))

post += ('published',) #same as post = post + ('published',)

print(id(post))

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)