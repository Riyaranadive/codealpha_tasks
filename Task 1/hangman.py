import random

# Predefined list of 5 words
word_list = ["apple", "tiger", "house", "plant", "river"]

# Randomly choose a word
word_to_guess = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Create a display version of the word with underscores
display_word = ["_" for _ in word_to_guess]

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_incorrect, "incorrect guesses allowed.")
print(" ".join(display_word))

# Main game loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess! You have", max_incorrect - incorrect_guesses, "guesses left.")

    print(" ".join(display_word))

# Game end
if "_" not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game over! The word was:", word_to_guess)
