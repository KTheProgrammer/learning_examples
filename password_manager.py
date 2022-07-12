from tkinter import *
from tkinter import messagebox
import random
import
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def new_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]

    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_label_en.delete(0, END)
    password_label_en.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def saved_file():
    if len(website_label_en.get()) < 1 or len(password_label_en.get()) < 1:
        messagebox.showerror("Error", "Fill in all Fields!")
    else:
        message_ok = messagebox.askokcancel("Ready to Save", f"You entered this Infomation:\n "
                                                   f"Email: {email_label_en.get()}\n Password: {password_label_en.get()}")
        if message_ok:
            with open("data.txt", mode="a") as completed_info:
                completed_info.write(f"{website_label_en.get()} | {email_label_en.get()} | {password_label_en.get()} \n")
                website_label_en.delete(0, END)
                password_label_en.delete(0, END)
                messagebox.showinfo("Saved Data", "Data saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

website_label_en = Entry(width=35)
website_label_en.grid(row=1, column=1, columnspan=2)
website_label_en.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_label_en = Entry(width=35)
email_label_en.grid(row=2, column=1, columnspan=2)
email_label_en.insert(0, "mikeviomcclellan@yahoo.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_label_en = Entry(width=21)
password_label_en.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=new_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=saved_file)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
