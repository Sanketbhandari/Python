print("Welcome to Sanket's pizza service!")

bill = 0

size = input("What type of pizza would you like s, m or l?\n").lower()

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

pepperoni = input("Do you want pepperoni y or n?\n").lower()
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
elif pepperoni == "n":
    pass

cheese = input("Do you want extra cheese y or n?\n").lower()
if cheese == "y":
    bill += 1
else:
    pass
print(f"You total bill is ${bill}")