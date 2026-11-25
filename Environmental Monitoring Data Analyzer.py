readings = []

days = int(input("Enter number of days: "))

for i in range(days):
    print("\nDay", i + 1)

    day_readings = []

    for j in range(3):
        value = float(input("Enter pollution reading: "))
        day_readings.append(value)

    readings.append(day_readings)

print("\nEnvironmental Report")

for i in range(days):
    average = sum(readings[i]) / 3

    print("\nDay", i + 1)
    print("Readings:", readings[i])
    print("Average:", average)

    if average < 50:
        print("Good Environment")
    elif average <= 100:
        print("Moderate Pollution")
    else:
        print("High Pollution")

print("\nOverall Average:")

total = 0
count = 0

for i in range(days):
    for j in range(3):
        total += readings[i][j]
        count += 1

print(total / count)