import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
    return user_choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "Congratulations! You win!"
    else:
        return "Computer wins. Better luck next time!"

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    