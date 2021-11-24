print("Welcome to the Tip Calculator!")
Total_bill= float(input("What was the total bill?\n$"))
Tip = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
split = int(input("How many people to split the bill?\n"))
Bill_with_tip = Total_bill+(Total_bill * Tip/100)
Split_bill = Bill_with_tip / split
print(f"Each have to pay ${round(Split_bill,2)}")