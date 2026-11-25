marks = []

for i in range(3):
    m = int(input("Enter exam marks: "))
    marks.append(m)

print("Examination marks:", marks)

improvement = marks[2] - marks[0]

print("Total marks:", sum(marks))
print("Average marks:", sum(marks) / 3)

if improvement > 0:
    print("Student performance improved")
elif improvement < 0:
    print("Student performance declined")
else:
    print("No change in performance")

if min(marks) < 35:
    print("Weak performance detected")
else:
    print("Good performance")