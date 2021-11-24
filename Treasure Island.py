print("Welcome to the Treasure Island!\nYour mission is to find the Treasure")
decision1 = input("Where do you want to go? left or right?\n").lower()

if decision1 == "left":
    decision2 = input("What you want to do? Swim or Wait?\n").lower()
    if decision2 == "wait":
        decision3 = input("Which colour door you will choose? Red, Blue or Yellow?\n").lower()
        if decision3 == "yellow":
            print("You win")
        else:
            print("Game over!")
    else:
        print("Game over!")
else:
    print("Game over!")