from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- Show Words ------------------------------- #
try:
    data = pd.read_csv("/Users/abhisheksabnivis/Desktop/100daysofcode/Day 31/flashcard_app/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("/Users/abhisheksabnivis/Desktop/100daysofcode/Day 31/flashcard_app/data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flashcard.itemconfig(card_title, text="French", fill="black")
    flashcard.itemconfig(card_word, text=current_card["French"], fill="black")
    flashcard.itemconfig(card_image, image=flash_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flashcard.itemconfig(card_title, text="English", fill="white")
    flashcard.itemconfig(card_word, text=current_card["English"], fill="white")
    flashcard.itemconfig(card_image, image=flash_back)


def is_known():
    to_learn.remove(current_card)
    #print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("/Users/abhisheksabnivis/Desktop/100daysofcode/Day 31/flashcard_app/data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

flashcard = Canvas(window, width=800, height=526, highlightthickness=0)
flash_front = PhotoImage(file='/Users/abhisheksabnivis/Desktop/100daysofcode/Day 31/flashcard_app/images/card_front.png')
flash_back = PhotoImage(file='/Users/abhisheksabnivis/Desktop/100daysofcode/Day 31/flashcard_app/images/card_back.png')
card_image = flashcard.create_image(400, 263, image=flash_front)
card_title = flashcard.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
card_word = flashcard.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")
flashcard.config(bg=BACKGROUND_COLOR)
flashcard.grid(column=0, row=0, columnspan=2)

right = PhotoImage(file="/Users/abhisheksabnivis/Desktop/100daysofcode/Day 31/flashcard_app/images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="/Users/abhisheksabnivis/Desktop/100daysofcode/Day 31/flashcard_app/images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()