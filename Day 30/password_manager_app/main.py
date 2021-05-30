from tkinter import * 
from tkinter import messagebox
from password import PasswordGenerator
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search():
    website = website_input.get()
    data_file = "/Users/abhisheksabnivis/Desktop/100daysofcode/Day 30/password_manager_app/data.json"
    try:
        with open(data_file, "r") as fl:
            contents = json.load(fl)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in contents:
            messagebox.showinfo(title=website, message=f"email: {contents[website]['email']}\npassword: {contents[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details found for {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    generator = PasswordGenerator()
    password_input.insert(0, generator.password)
    pyperclip.copy(generator.password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    site = website_input.get()
    email = email_input.get()
    password = password_input.get()
    data_json = {
        site: {
            "email": email,
            "password": password
        }
    }
    
    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields blank")
    else:
        file_name = "/Users/abhisheksabnivis/Desktop/100daysofcode/Day 30/password_manager_app/data.json"
        try:
            with open(file_name, "r") as file:
                #Reading Old Data
                data = json.load(file)
        except FileNotFoundError:
            with open(file_name, "w") as f:
                json.dump(data_json, f, indent=4)
        else:
            #Appending new data to it
            data.update(data_json)
            with open(file_name, "w") as files:
                #Saving updated data
                json.dump(data, files, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas with mypass image
canvas = Canvas(width=200, height=200)
img = PhotoImage("/Users/abhisheksabnivis/Desktop/100daysofcode/Day 30/password_manager_app/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry()
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "abhisabnives@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

search_password = Button(text="Search", width=10, command=search)
search_password.grid(column=2, row=1)

generate_password = Button(text="Generate Password", width=10, command=generate)
generate_password.grid(column=2, row=3)

add_password = Button(text="Add", width=36, command=save_password)
add_password.grid(column=1, row=4, columnspan=2)

window.mainloop()