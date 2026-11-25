items = ["Burger", "Pizza", "Sandwich"]
prices = [50, 100, 40]
stock = [20, 15, 25]

sales = 0

n = int(input("Enter number of orders: "))

for i in range(n):
    print("\nAvailable Items:")

    for j in range(3):
        print(j + 1, items[j], "- Rs.", prices[j],
              "Stock:", stock[j])

    choice = int(input("Select item (1-3): "))
    quantity = int(input("Enter quantity: "))

    if choice < 1 or choice > 3 or quantity <= 0:
        print("Invalid order")

    elif quantity > stock[choice - 1]:
        print("Insufficient stock")

    else:
        index = choice - 1

        bill = prices[index] * quantity
        stock[index] -= quantity
        sales += bill

        print("Order successful")
        print("Item:", items[index])
        print("Bill amount: Rs.", bill)

print("\nDaily Sales: Rs.", sales)

print("\nRemaining Stock:")
for i in range(3):
    print(items[i], ":", stock[i])