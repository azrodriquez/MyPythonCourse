product1_price = input("What is the price of product 1? ")
print('the type is', type(product1_price))
print('product1_price is: ', product1_price)
price1 = float(product1_price)
print('Product 1 is an integer: ', price1.is_integer())
weight1 = float(input("How many ounces is product 1? "))
price2 = float(input("What is the price of product 2? "))
weight2 = float(input("How many ounces is product 2 "))
price_per_ounce1 = price1 / weight1
price_per_ounce2 = price2 / weight2
print("Price per ounce of product 1: ")
print(price_per_ounce1)
print("Price per ounce of product 2: ")
print(price_per_ounce2)
print(price_per_ounce1 < price_per_ounce2)
print(price_per_ounce1 > price_per_ounce2)
print(price1==price2)


import math
totalsum = price1 + price2
print(totalsum)
print("The discount price is: $" + totalsum * .10)
print("The truncated value of product1 is: ")
print("The truncated value is: " + math.trunc(price1))
print("The rounded value is: " + math.round(price1,1))
print("The floor value is: " + math.floor(price1))
print("The ceiling value is: " + math.ceil(price1))
