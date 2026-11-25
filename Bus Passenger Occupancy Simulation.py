capacity = int(input("Enter bus capacity: "))
passengers = 0

n = int(input("Enter number of stops: "))

for i in range(n):
    print("\nStop", i + 1)

    boarding = int(input("Passengers boarding: "))
    alighting = int(input("Passengers getting down: "))

    if boarding < 0 or alighting < 0:
        print("Invalid passenger count")
        continue

    if alighting > passengers:
        print("Invalid: More passengers getting down")
    else:
        passengers -= alighting
        passengers += boarding

        print("Current passengers:", passengers)

        if passengers > capacity:
            print("Bus capacity exceeded!")
        else:
            print("Bus capacity is available")

print("\nFinal passengers:", passengers)
print("Available seats:", capacity - passengers)