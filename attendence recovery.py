total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    percentage = attended / total * 100
    print("Attendance:", percentage, "%")

    if percentage >= 75:
        print("You are eligible")
    else:
        required = 0
        while percentage < 75:
            total += 1
            attended += 1
            required += 1
            percentage = attended / total * 100

        print("You need to attend", required, "more classes")
        print("New attendance:", percentage, "%")