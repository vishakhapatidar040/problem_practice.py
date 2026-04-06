#shopping bill generator
item1 = input("Enter the name of the first item: ")
price1 = float(input("Enter the price of the first item: "))
quantity1 = int(input("Enter the quantity of the first item: "))

item2 = input("Enter the name of the second item: ")
price2 = float(input("Enter the price of the second item: "))
quantity2 = int(input("Enter the quantity of the second item: "))

item3 = input("Enter the name of the third item: ")
price3 = float(input("Enter the price of the third item: "))
quantity3 = int(input("Enter the quantity of the third item: "))

total_cost = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
print("\nShopping Bill")
print(f"{item1}: {quantity1} x {price1} = {price1 * quantity1}")
print(f"{item2}: {quantity2} x {price2} = {price2 * quantity2}")
print(f"{item3}: {quantity3} x {price3} = {price3 * quantity3}")
print("Total Cost:", total_cost)        
