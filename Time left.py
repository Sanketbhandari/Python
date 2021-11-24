age = input("What is your current age?\n")
Time_left = 90 - int(age)
Days = Time_left*365
Months = Time_left*12
Weeks = Time_left*52

print(f"You have {Months} months, {Weeks} weeks and {Days} days left")