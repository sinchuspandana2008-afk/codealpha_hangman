import random

WORDS = ["python", "coding", "laptop", "internet", "program"]
MAX_WRONG = 6


def show_word(word, guessed):
    """Show the word with _ for letters not guessed yet."""
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def main():
    word = random.choice(WORDS)
    guessed = []          # all letters guessed so far
    wrong_guesses = 0

    print("=== Hangman Game ===")
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong_guesses < MAX_WRONG:
        print("Word:", show_word(word, guessed))
        print("Guessed letters:", " ".join(guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")

        guess = input("Enter a letter: ").lower().strip()

        # Check the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

        # Check if the player has won
        if all(letter in guessed for letter in word):
            print("Word:", show_word(word, guessed))
            print("Congratulations! You won! 🎉")
            break
    else:
        print("Game over! You lost.")
        print("The word was:", word)
if __name__=="__main__":
    main()