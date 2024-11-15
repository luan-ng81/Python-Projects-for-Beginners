import random

def number_guessing_game():
    result = random.randint(1,100)
    print("ans:", result)
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            if int(guess) > result:
                print("Too high!")
            elif int(guess) < result:
                print("Too low!")
            else:
                print("Congratulations! You guessed the number.")
                break
        except ValueError:
            print("Please enter a valid number")
        

    
number_guessing_game()