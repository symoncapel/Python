sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

#sale_prices.sort()
#print(sale_prices)
#[1, 3, 10, 40, 83, 100, 100, 220, 400]

#sorted_list = sale_prices.sort()
#print(sale_prices)
#None

sorted_list = sorted(sale_prices)
print(sorted_list)
#[1, 3, 10, 40, 83, 100, 100, 220, 400] doesnt effect the list

sorted_list = sorted(sale_prices, reverse=True)
print(sorted_list)
#[400, 220, 100, 100, 83, 40, 10, 3, 1]