from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- CONSTANTS ------------------------------- #
DEFAULT_EMAIL = "omer@email.com"
# ----------------------------------------------------------------------- #


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ----------------------------------------------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if website == "" or website.isspace():
        messagebox.showinfo(title="Error", message="Website is missing")
    elif username == "" or username.isspace():
        messagebox.showinfo(title="Error", message="Username is missing")
    elif password == "" or password.isspace():
        messagebox.showinfo(title="Error", message="Password is missing")
    else:
        is_okay_to_save = messagebox.askokcancel(title=website,
                                                 message=f"Website: {website}\n"
                                                         f"Email: {username}\n"
                                                         f"Password: {password}\n\n"
                                                         f"Save?")
        if is_okay_to_save:
            data = None
            new_data = {website: {'username': username, 'password': password}}
            try:
                data_file = open('data.json', 'r')
            except FileNotFoundError:
                data = new_data
            else:
                data = json.load(data_file)
                data.update(new_data)
            finally:
                data_file = open('data.json', 'w')
                json.dump(data, data_file, indent=4)
                data_file.close()
                entries_default_values()
# ----------------------------------------------------------------------- #


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pass():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        website = website_input.get()
        try:
            password = data[website]['password']
            username = data[website]['username']
        except KeyError:
            messagebox.showinfo(title="Error", message=f"No password linked to {website}.")
        else:
            messagebox.showinfo(title=website,
                                message=f"Website: {website}\n"
                                        f"Email: {username}\n"
                                        f"Password: {password}\n")
# ---------------------------------------------------------------------------- #


# ---------------------------- ENTRIES VALUES RESET ------------------------------- #
def entries_default_values():
    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)
    username_input.insert(0, DEFAULT_EMAIL)
# ---------------------------------------------------------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
# ---------------------Window---------------#
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# -------------------------------------------- #


# -----------------Canvas------------------ #
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# -------------------------------------------- #


# ---------------Buttons--------------------- #
generate_pass_button = Button(text="Generate Password", width=10, command=generate_pass)
add_button = Button(text="Add", width=34, command=save)
search_button = Button(text="Search", width=10, command=search_pass)

generate_pass_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)
# -------------------------------------------- #


# ---------------Entries--------------------- #
website_input = Entry(width=21)
username_input = Entry(width=36)
password_input = Entry(width=21)

website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()
username_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)

entries_default_values()
# -------------------------------------------- #


# ------------------Labels---------------------- #
website_text = Label(text="Website:")
username_text = Label(text="Email/Username:")
password_text = Label(text="Password:")

website_text.grid(row=1, column=0)
username_text.grid(row=2, column=0)
password_text.grid(row=3, column=0)
# --------------------------------------------- #

window.mainloop()
