print("Welcome to Sanket's Roller Coaster!")

height = int(input("What is your height in cm?\n"))
bill = 0
if height > 120:
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    else:
        bill = 12
    pic = input("Would you like to capture photo?\n")
    if pic == "yes" or pic == "Yes":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("You are not eligible for the ride!")