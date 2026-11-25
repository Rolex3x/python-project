marks = []
attendance = []
lab = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    m = int(input("Enter marks: "))
    a = float(input("Enter attendance percentage: "))
    l = int(input("Enter lab marks: "))

    marks.append(m)
    attendance.append(a)
    lab.append(l)

    risk = 0

    if m < 40:
        risk += 1

    if a < 75:
        risk += 1

    if l < 40:
        risk += 1

    if risk == 0:
        print("Low Risk")
    elif risk == 1:
        print("Medium Risk")
    else:
        print("High Risk")

print("\nStudent Summary")

for i in range(n):
    print("Student", i + 1)
    print("Marks:", marks[i])
    print("Attendance:", attendance[i])
    print("Lab Marks:", lab[i])