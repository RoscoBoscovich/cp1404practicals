
"""SHOP CALCULATOR"""

item_number= int(input("Enter number of items:"))

while  item_number < 0:
    print("Invalid number of items")
    item_number = int(input("Enter number of items:"))

total_cost = 0
for i in range(item_number):
    price = float(input("Price of item:"))
    total_cost = total_cost + price

    if total_cost >= 100:
        total_cost = total_cost*0.9

print("Total price for",item_number,"items is $",total_cost)