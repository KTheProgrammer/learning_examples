from tkinter import *


def button_clicked():
    new_text = input_mile.get()
    distance = int(new_text) * 1.609344
    num.config(text=f"{int(distance)}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

#Input
input_mile = Entry(width=7)
input_mile.grid(column=2, row=0)

#Label
mile = Label(text="Miles")
mile.grid(column=3, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=2)

num = Label(text="0")
num.grid(column=2, row=2)

km = Label(text="KM")
km.grid(column=3, row=2)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()
