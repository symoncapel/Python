def heading_generator(title, heading_type):
    return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('Greeting', '1'))
print(heading_generator('Hey there', '3'))