import random

game_winning_rules = """Winning Rules of the Rock paper and scissor game as follows
rock vs paper->paper wins (paper covers rock)
rock vs scissors->rock wins (rock smashes scissors)
paper vs scissors->scissors wins(scissors cut paper)
"""
print(game_winning_rules)
print("\n")

game_choices = """
Enter choice 
1. Rock
2. Paper
3. Scissor
"""

choices_dict = {1:"Rock", 2:"Paper", 3:"Scissor"}

while True:
    user_choice = ""

    try:
        # code that may cause errors
        user_choice = int(input(game_choices))
    except ValueError as error:
        # code that handle exceptions
        print("Error! Invalid choice")
        continue
    else:
        # code that executes when no exception occurs
        # Check if user input is within range
        if user_choice < 1 or user_choice > 3:
            print("Must be between 1 through to 3")
            continue

        # If everything is okay
        print(f"User turn: {choices_dict[user_choice]}")
        computer_choice = random.randint(1, 3)

        print("Now it\'s computer turn...")

        print(f"Computer turn: {choices_dict[computer_choice]}")

        print("User vs Computer: \n"  + choices_dict[user_choice] + " vs " + choices_dict[computer_choice])

        if choices_dict[user_choice] == "Rock" and choices_dict[computer_choice] == "Paper":
            print("Paper wins => Computer wins")
        if choices_dict[user_choice] == "Paper" and choices_dict[computer_choice] == "Rock":
            print("Paper wins => User wins")
        elif choices_dict[user_choice] == "Rock" and choices_dict[computer_choice] == "Scissor":
            print("Rock wins => User wins")
        elif choices_dict[user_choice] == "Paper" and choices_dict[computer_choice] == "Scissor":
            print("Scissors wins => Computer wins")
        elif choices_dict[user_choice] == "Scissor" and choices_dict[computer_choice] == "Paper":
            print("Scissors wins => User wins")
        elif choices_dict[user_choice] == "Scissor" and choices_dict[computer_choice] == "Rock":
            print("Rock wins => Computer wins")
        else:
            print("Draw: " + choices_dict[user_choice] + " == " + choices_dict[computer_choice])

        break

