import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_to_guess = random.choice(word_list).upper()
        self.display_word = ['_' if letter.isalpha() else letter for letter in self.word_to_guess]
        self.guesses_left = 6
        self.guessed_letters = set()

    def display_board(self):
        print(" ".join(self.display_word))
        print(f"Guesses Left: {self.guesses_left}")
        print(f"Guessed Letters: {' '.join(sorted(self.guessed_letters))}")

    def make_guess(self, guess):
        guess = guess.upper()

        if guess.isalpha() and len(guess) == 1:
            if guess in self.guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in self.word_to_guess:
                print("Good guess!")
                self.update_display_word(guess)
            else:
                print("Incorrect guess.")
                self.guesses_left -= 1

            self.guessed_letters.add(guess)
        else:
            print("Invalid input. Please enter a single alphabet letter.")

    def update_display_word(self, guess):
        for i, letter in enumerate(self.word_to_guess):
            if letter == guess:
                self.display_word[i] = guess

    def check_game_status(self):
        if '_' not in self.display_word:
            print("Congratulations! You guessed the word:", self.word_to_guess)
            return True
        elif self.guesses_left == 0:
            print("Sorry, you ran out of guesses. The word was:", self.word_to_guess)
            return True
        else:
            return False

def main():
    words = ["PYTHON", "JAVA", "CPLUSPLUS", "JAVASCRIPT", "HTML", "CSS", "GITHUB", "PROGRAMMING"]
    hangman_game = HangmanGame(words)

    print("Welcome to Hangman!")
    while not hangman_game.check_game_status():
        hangman_game.display_board()
        guess = input("Enter your guess: ")
        hangman_game.make_guess(guess)

if __name__ == "__main__":
    main()
    