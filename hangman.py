import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import random

word_list = ["apple", "tiger", "house", "plant", "river"]

def start_new_game():
    global word_to_guess, guessed_letters, incorrect_guesses, display_word

    word_to_guess = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    display_word = ["_" for _ in word_to_guess]

    update_display()
    message_label.config(text="Guess a letter...")
    guess_entry.config(state='normal')
    guess_button.config(state='normal')
    update_hangman_image()

def check_guess():
    global incorrect_guesses

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if not guess.isalpha() or len(guess) != 1:
        message_label.config(text="Please enter one letter.")
        return

    if guess in guessed_letters:
        message_label.config(text=f"You already guessed '{guess}'.")
        return

    guessed_letters.append(guess)

    if guess in word_to_guess:
        message_label.config(text="🎉 Nice guess!")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        message_label.config(text=f"❌ Wrong! {6 - incorrect_guesses} left.")
        update_hangman_image()

    update_display()
    check_game_over()

def update_display():
    word_label.config(text=" ".join(display_word))
    guessed_label.config(text="Guessed: " + ", ".join(guessed_letters))

def update_hangman_image():
    hangman_img = hangman_images[incorrect_guesses]
    hangman_label.config(image=hangman_img)
    hangman_label.image = hangman_img

def check_game_over():
    if "_" not in display_word:
        message_label.config(text=f"🎉 You won! Word: {word_to_guess}")
        end_game()
    elif incorrect_guesses >= 6:
        message_label.config(text=f"💀 Game over! Word: {word_to_guess}")
        end_game()

def end_game():
    guess_entry.config(state='disabled')
    guess_button.config(state='disabled')

# --- Setup Tkinter ---
root = tk.Tk()
root.title("Cartoon Hangman")
root.geometry("1920x960")

# Background
bg_image = Image.open("background .jpg").resize((1920, 960))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load hangman images
hangman_images = []
for i in range(7):
    img = Image.open(f"hangman{i}.jpg").resize((120, 120))
    hangman_images.append(ImageTk.PhotoImage(img))

# UI Elements
title_label = tk.Label(root, text="Hangman Game", font=("Comic Sans MS", 32, "bold"), bg="#49abe4", fg="#1b1b2f")
title_label.pack(pady=10)

hangman_label = tk.Label(root, bg="#5bb7f5")
hangman_label.pack(pady=20)

word_label = tk.Label(root, text="", font=("Courier", 28, "bold"), bg="#7ec2e9")
word_label.pack(pady=10)

guessed_label = tk.Label(root, text="", font=("Arial", 12), bg="#49abe4")
guessed_label.pack()

guess_entry = tk.Entry(root, font=("Helvetica", 18), width=3, justify='center')
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", font=("Comic Sans MS", 14), command=check_guess, bg="#8ecae6")
guess_button.pack(pady=20)

message_label = tk.Label(root, text="", font=("Comic Sans MS", 14), bg="#d4f1f4", fg="darkblue")
message_label.pack(pady=10)

restart_button = tk.Button(root, text="New Game", font=("Comic Sans MS", 24), command=start_new_game, bg="#ffb703")
restart_button.pack(pady=80)

start_new_game()
root.mainloop()
