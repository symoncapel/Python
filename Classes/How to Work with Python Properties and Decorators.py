class Invoice:

    def __init__(self, client,total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total


google = Invoice('Google', 100)
print(google.client)
google.client = 'Yahoo'
print(google.client)


'''
Coding Exercise
We want to ensure that our size attribute can be retrieved, but not set. Use the appropriate syntax to protect the size attribute. Then, use the 'property' decorator to build a getter to return the protected data. You do not need to instantiate the class.
'''
class Garage:
  def __init__(self, size):
    #   Protect the size attribute
    self._size = size
    self.cars = []

  @property
  def size(self):
    return self._size

  def open_door(self):
    return "The door opens"