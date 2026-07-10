import random

WORDS = ["python", "hangman", "computer", "keyboard", "science"]
MAX_WRONG_GUESSES = 6


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_game():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("\nWelcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have", MAX_WRONG_GUESSES, "wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word: " + display_word(word, guessed_letters))
        print("Guessed letters: " + ", ".join(guessed_letters))
        print("Wrong guesses: " + str(wrong_guesses) + "/" + str(MAX_WRONG_GUESSES))

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

        won = True
        for letter in word:
            if letter not in guessed_letters:
                won = False

        if won:
            print("Congratulations! You guessed the word: " + word)
            return

    print("You lost! The word was: " + word)


def main():
    play_again = "yes"

    while play_again == "yes":
        play_game()
        answer = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if answer == "yes":
            play_again = "yes"
        else:
            play_again = "no"

    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()
