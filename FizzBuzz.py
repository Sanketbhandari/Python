First_number = int(input("Please input the starting number:\n"))
Second_number = int(input("Please input the Final number:\n"))

for number in range(First_number,Second_number+1):
    if number%3 == 0 and number%5 == 0:
        print("fizzbuzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)