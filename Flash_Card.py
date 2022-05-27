from tkinter import *
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
all_words = data.to_dict()
print(all_words["French"][0])
print(all_words["English"][0])


def correct():
    print("Green Clicked")


def wrong_answer():
    print("Red Clicked")


window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=820, height=550, background=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(410, 280, image=front_card)
canvas.create_text(410, 190, text="French", font=("courier", 35, "normal"))
counter = canvas.create_text(410, 270, text=f"{all_words['French'][0]}", font=("courier", 40, "bold"))
canvas.pack()

wrong_button = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_button, highlightthickness=0, command=wrong_answer)
wrong.pack(side="left", expand=1)

right_button = PhotoImage(file="./images/right.png")
right = Button(image=right_button, highlightthickness=0, command=correct)
right.pack(side="left", expand=1)


window.mainloop()
