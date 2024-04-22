import json
import tkinter.messagebox

def save(platform, email, password):
    platform_text = platform.get()
    email_text = email.get()
    password_text = password.get()
    if platform_text == "" or password_text == "":
        tkinter.messagebox.showerror(title="Error", message="Please specify platform and password")
        return
    item = {platform_text: {"email": email_text, "password": password_text}}
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
