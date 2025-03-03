from tkinter import *
import tkinter.font
import pandas as pd
import random

# -------------------------------------- CONSTANTS -------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'
# --------------------------------------------------------------------------------------- #


# -------------------------------------- FUNCTIONS -------------------------------------- #
def known_word():
    to_learn.remove(current_word)
    updated_data = pd.DataFrame(to_learn)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global flip_timer, current_word
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)

    canvas.itemconfig(card_image, image=CARD_FRONT_IMAGE)
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_word['French'], fill='black')

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_word['English'], fill='white')
    canvas.itemconfig(card_image, image=CARD_BACK_IMAGE)
# --------------------------------------------------------------------------------------- #


# -------------------------------------- UI SETUP -------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
CHECK_MARK_IMAGE = PhotoImage(file="images/right.png")
X_MARK_IMAGE = PhotoImage(file="images/wrong.png")
CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")
CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Buttons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
check_mark_button = Button(image=CHECK_MARK_IMAGE, highlightthickness=0, borderwidth=0,
                           command=known_word)
x_mark_button = Button(image=X_MARK_IMAGE, highlightthickness=0, borderwidth=0,
                       command=next_card)

check_mark_button.grid(row=1, column=1)
x_mark_button.grid(row=1, column=0)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Canvas ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=CARD_FRONT_IMAGE)
language_text = canvas.create_text(400, 160, text="Title",
                                   font=tkinter.font.Font(family=FONT_NAME, size=50, slant='italic'))
word_text = canvas.create_text(400, 300, text="Word",
                               font=tkinter.font.Font(family=FONT_NAME, size=70, weight='bold'))

canvas.grid(row=0, column=0, columnspan=2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

data = None

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient='records')


flip_timer = window.after(3000, next_card)
current_word = {}

next_card()


window.mainloop()
# -------------------------------------------------------------------------------------- #
