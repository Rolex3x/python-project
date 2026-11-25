prepared = []
served = []
wasted = []

n = int(input("Enter number of days: "))

for i in range(n):
    print("\nDay", i + 1)

    p = int(input("Meals prepared: "))
    s = int(input("Meals served: "))

    if p < 0 or s < 0 or s > p:
        print("Invalid details")
        continue

    w = p - s

    prepared.append(p)
    served.append(s)
    wasted.append(w)

    percentage = (w / p) * 100 if p > 0 else 0

    print("Meals wasted:", w)
    print("Wastage percentage:", percentage, "%")

    if percentage > 20:
        print("High food wastage")
    else:
        print("Acceptable food wastage")

print("\nTotal prepared:", sum(prepared))
print("Total served:", sum(served))
print("Total wasted:", sum(wasted))