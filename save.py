import json
import tkinter.messagebox
import pyperclip

def save(platform, username, phone_number, email, password):
    platform_text = platform.get()
    username_text = username.get()
    phone_number_text = phone_number.get()
    email_text = email.get()
    password_text = password.get()
    if platform_text == "" or password_text == "":
        tkinter.messagebox.showerror(title="Error", message="Please specify platform and password")
        return
    item = {platform_text: {"email": email_text, "password": password_text, "phone_number": phone_number_text, "username": username_text}}
    try:
        with open("data.json", "r") as password_data:
            passwords = json.load(password_data)
            passwords.update(item)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            passwords = {}
            passwords.update(item)

    with open("data.json", "w") as password_data:
        json.dump(passwords, password_data, indent=4)
    tkinter.messagebox.showinfo(title="Success", message="Information has been successfully saved.")
    password.delete(0, "end")
    email.delete(0, "end")
    platform.delete(0, "end")
    username.delete(0, "end")
    phone_number.delete(0, "end")
    pyperclip.copy(password_text)
    