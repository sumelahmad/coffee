# menu = {
#     'pizza': 550,
#     'pasta': 300,
#     'burger': 390,
#     'salad': 100,
#     'coffee': 120,
# }
#
# print("Welcome to my Restaurant")
# print('Pizza: TK 550\nPasta: TK 300\nBurger: TK 390\nSalad: TK 100\nCoffee: TK 120')
#
# order_total = 0
#
#
# item_1 = input('Enter the name of the item you want to order: ')
# if item_1 in menu:
#     order_total += menu[item_1]
#     print(f"Your item {item_1} has been added")
# else:
#     print(f"Your chosen item {item_1} is not available")
#
#
# another_order = input("Do you want another order? (Yes/No): ")
# if another_order.lower() == "yes":
#     item_2 = input('Enter the name of the second item: ')
#     if item_2 in menu:
#         order_total += menu[item_2]
#         print(f"Item {item_2} has been added")
#     else:
#         print(f"Your chosen item {item_2} is not available")
#
#
# print(f"The total amount to pay is {order_total} TK")



menu = {
    'pizza': 550,
    'pasta': 300,
    'burger': 390,
    'salad': 100,
    'coffee': 120,
}

print("Welcome to my Restaurant")
print('Pizza: TK 550\nPasta: TK 300\nBurger: TK 390\nSalad: TK 100\nCoffee: TK 120')

order_total = 0

while True:
    item = input('Enter the name of the item you want to order: ')
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added.")
    else:
        print(f"Your chosen item {item} is not available.")

    another_order = input("Do you want to order another item? (yes/no): ")
    if another_order != "yes":
        break


print(f"The total amount to pay is {order_total} TK")
