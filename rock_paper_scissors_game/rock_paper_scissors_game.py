import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emoji = {ROCK: "🪨", PAPER: "📃", SCISSORS: "✂️"}
choices = tuple(emoji.keys())

def get_user_choice():
    while True:        
        user_choice = input("Rock, paper, or scissors? (r/p/s): ")
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("tie")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == SCISSORS and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK)):
        print("You win")
    else:
        print("you lose")


def rock_paper_scissors_game():

    should_continue = True

    while should_continue:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        print(f"You chose: {emoji[user_choice]}")
        print(f"computer chose: {emoji[computer_choice]}")
        
        determine_winner(user_choice, computer_choice)

        respond = input("Continue? (y/n):").lower()
        if respond == "y":
            continue
        if respond == "n":
            should_continue = False

    


rock_paper_scissors_game()