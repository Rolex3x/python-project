password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Strong password")
else:
    print("Weak password")

    if len(password) < 8:
        print("Minimum 8 characters required")
    if not upper:
        print("Include an uppercase letter")
    if not lower:
        print("Include a lowercase letter")
    if not digit:
        print("Include a number")
    if not special:
        print("Include a special character")