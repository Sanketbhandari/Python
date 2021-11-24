First_number = int(input("Please input the starting number:\n"))
Second_number = int(input("Please input the Final number:\n"))

even_sum = 0
for number in range(First_number,Second_number+1):
    if number%2 == 0:
        even_sum += number
print(f"The total sum of even numbers in the range {First_number} to {Second_number} is: {even_sum}")