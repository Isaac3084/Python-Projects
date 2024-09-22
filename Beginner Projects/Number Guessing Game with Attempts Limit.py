import random

def number_guessing_game(attempts):
    number = random.randint(1, 100)
    while attempts > 0:
        guess = int(input("Guess the number (1-100): "))
        if guess == number:
            print("Congratulations! You guessed the correct number.")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
        print(f"Attempts remaining: {attempts}")
    print(f"Sorry, you're out of attempts! The number was {number}.")
number_guessing_game(5)
