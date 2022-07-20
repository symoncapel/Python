#__repr__
# Dunder repr is used more for raw output so you usually do not format it nicely. It's something that you would do like output to your logs or to an error log or something like that.


class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f'Invoice from {self.client} for ${self.total}'

    def __repr__(self):
        return f'Invoice < values: client: {self.client}, total: {self.total}>'

inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))

'''
So my rule of thumb is whenever I use repr I wrap up all the attributes any kind of data that I know I'm going to need to use whenever I'm performing debugging and then it can be a very helpful tool both for logs and also when I'm trying to fix a bug in a program.
'''