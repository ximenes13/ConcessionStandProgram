menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 5.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0

print("--------------- MENU ---------------")
for key, value in menu.items():
    print(f"{key} : {value:.2f}€")
print("------------------------------------")


print("------------ YOUR ORDER ------------")
while True:
    food = input("Select an option: (q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food):
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print("------------------------------------")


print(cart)
print(f"Total is: {total}€")