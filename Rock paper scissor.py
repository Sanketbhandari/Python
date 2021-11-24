import random

player_choice = int(input("What you want to choose? Type 0 for rock, 1 for paper or 2 for scissor\n"))
computer_choice = random.randint(0,2)

if player_choice == 0 and computer_choice == 1:
    print(f"Computer choose {computer_choice}, Computer wins")
elif player_choice == 0 and computer_choice == 2:
    print(f"Computer choose {computer_choice}, player wins")
elif player_choice == 1 and computer_choice == 0:
    print(f"Computer choose {computer_choice}, Player wins")
elif player_choice == 1 and computer_choice == 2:
    print(f"Computer choose {computer_choice}, Computer wins")
elif player_choice == 2 and computer_choice == 0:
    print(f"Computer choose {computer_choice}, Computer wins")
elif player_choice == 2 and computer_choice == 1:
    print(f"Computer choose {computer_choice}, player wins")
elif player_choice == computer_choice:
    print(f"Computer choose {computer_choice}, match draw")
else:
    print("please choose a valid option")

