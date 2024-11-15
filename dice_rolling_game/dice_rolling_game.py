import random


def dice_rolling_game():
    first, second = 0, 0
    while True:
        response = input("Roll the dice? (y/n): ").lower()
        if response == "y":
            first = random.randint(1,6)
            second = random.randint(1,6)
            print(f"({first}, {second})")
        elif response == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")

dice_rolling_game()