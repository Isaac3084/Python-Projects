import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I've selected a random number between 1 and 100. Can you guess it?")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
