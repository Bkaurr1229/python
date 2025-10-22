import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

def search():
    # Used exception Handleing
    website = entry_website.get()
    try:
        with open("password.json", "r") as file:
            data = json.load(file)

    except:
        messagebox.showinfo(title="Error", message="No data file found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\n Password: {password} ")

        else:
            messagebox.showinfo(title="Error",message="no details found")



    # messagebox.showinfo(title=entry_website, message=)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = entry_email.get()
    password = entry.get()
    website = entry_website.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    # USED MESSAGEBOX
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="OOPS", message=" The details are incompelete")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\n Email:{email} \n Password:{password}\n"
                                               f"Is it ok to save?")
        if is_ok:
            try:
                with open("password.json", "r") as file:
                    data = json.load(file)

            except:
                with open("password.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)
                with open("password.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                # making the data clear form the window to add another
                entry_website.delete(0, END)
                entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)

logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Webiste
label_website = Label(text="Webiste", font=(FONT_NAME, 15, "bold"))
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username", font=(FONT_NAME, 15, "bold"))
label_email.grid(column=0, row=2)
label_password = Label(text="Password", font=(FONT_NAME, 15, "bold"))
label_password.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=3, sticky="ew")
entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=3, sticky="ew")
entry_email.insert(0, "angela@gmail.com")
entry = Entry(width=21)
entry.grid(column=1, row=3, columnspan=1, sticky="ew")

button = Button(text="Search", command=search)
button.grid(column=3, row=1)

button = Button(text="Generate Password", command=generate_password)
button.grid(column=3, row=3)

button = Button(text="Add", width=36, command=save)
button.grid(column=1, row=4, columnspan=3, sticky="ew")

window.mainloop()
