import time
from tkinter import *
from pandas import *
import random

data = read_csv("data/french_words.csv")
data.to_csv("data/french_words.csv")


word = ""

def choose():
    x = 0
    global eng_word
    global word

    words_dict = {row.French:row.English for (index, row) in data.iterrows()}
    word = random.choice(list(words_dict.keys()))
    eng_word = words_dict[word]
    canvas.itemconfig(word_text, text=word, fill="black")


window = Tk()
window.title("Fishy")
window.config(padx=50, pady=50, bg="#B1DDC6")

canvas = Canvas(width=800, height=524, bg="#B1DDC6", highlightthickness=0)
card_png = PhotoImage(file="images/card_front.png")
back_png = PhotoImage(file="images/card_back.png")
canvas_card = canvas.create_image(400, 262, image=card_png)
canvas.grid(row=0, column=0, columnspan=2)
canvas.update()

language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 40, "bold"))



def change():
        canvas.itemconfig(canvas_card, image=back_png)
        canvas.itemconfig(language_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=eng_word, fill="white")


def change_back():
    canvas.itemconfig(canvas_card, image=card_png)
    canvas.itemconfig(language_text, text="French", fill="black")
    choose()
    window.after(3000, change)


def knew_it():
    global word
    if word != "":

        data = read_csv("data/french_words.csv", index_col="French")
        data.drop(word, inplace=True)
        data.to_csv("data/french_words.csv")
    change_back()

wrong_png = PhotoImage(file="images/wrong.png")
butt_no = Button(image=wrong_png, highlightthickness=0, command=change_back)
butt_no.grid(row=1, column=0)

right_png = PhotoImage(file="images/right.png")
butt_yes = Button(image=right_png, highlightthickness=0, command=knew_it)
butt_yes.grid(row=1, column=1)

window.mainloop()
data.to_csv("data/french_words.csv", index=False)
