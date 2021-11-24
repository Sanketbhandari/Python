print("Welcome to the Love calculator!")

name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

combined_name = name1 + name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

count1 = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
count2 = l + o + v + e

love_score = int(str(count1)+str(count2))
if love_score>90 or love_score<10:
    print(f"Your score is {love_score}, you go like coke and mentos.")
elif 50<love_score>40:
    print(f"Your score is {love_score}, you are aright together.")
else:
    print(f"Your love score is {love_score}")
