from decimal import Decimal

product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost)) #removes the decimal
print(float(qty)) # gives you a decimal for a float
print(Decimal(product_cost)) # gives you high level percision with the decimal
print(complex(commission_rate)) #scintific_notation gives you an object you can use