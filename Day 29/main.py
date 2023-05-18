import random
import string
import tkinter
import pyperclip
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters_string = [random.choice(string.ascii_letters) for _ in range(random.randint(8, 10))]
    numbers_string = [random.choice(string.digits) for _ in range(random.randint(2, 4))]
    punctuation_string = [random.choice(string.punctuation) for _ in range(random.randint(2, 4))]
    password_list = letters_string + numbers_string + punctuation_string
    random.shuffle(password_list)
    pass_text.delete(0, tkinter.END)
    new_password = ''.join(password_list)
    pass_text.insert(0, new_password)
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    site = site_text.get()
    mail = mail_text.get()
    passw = pass_text.get()
    if not all([site, passw]):
        messagebox.showinfo(message='No data to save.')
        return
    is_ok = messagebox.askokcancel(title=site, message=f'These are the details entered: \nEmails: {mail} \n'
                                                       f'Password: {passw} \nIs it ok to save?')
    if is_ok:
        with open('data.txt', 'a') as file:
            file.write(f'{site}' + ' | ' + f'{mail_text.get()}' + ' | ' + f'{pass_text.get()}\n')
        site_text.delete(0, tkinter.END)
        pass_text.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)

image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=1)

website = tkinter.Label(text="Website", font=("Arial", 15))
website.grid(column=0, row=2)
site_text = tkinter.Entry(width=40)
site_text.grid(column=1, row=2, columnspan=2)
site_text.focus()

email = tkinter.Label(text="Email/Username", font=("Arial", 15))
email.grid(column=0, row=3)
mail_text = tkinter.Entry(width=40)
mail_text.grid(column=1, row=3, columnspan=2)
mail_text.insert(0, 'aaa@gmail.com')

password = tkinter.Label(text="Password", font=("Arial", 15))
password.grid(column=0, row=4)
pass_text = tkinter.Entry(width=21)
pass_text.grid(column=1, row=4)
generate = tkinter.Button(text="Generate password", width=15, command=generate_password)
generate.grid(column=2, row=4, columnspan=3)

add = tkinter.Button(text="Add", width=37, command=save_data)
add.grid(column=1, row=5, columnspan=3)

window.mainloop()
