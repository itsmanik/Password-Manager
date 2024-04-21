import json
import tkinter.messagebox

def save(platform, email, password):
    if platform == "" or password == "":
        tkinter.messagebox.showerror(title="Error", message="Please specify platform and password")
        return
    item = {platform: {"email": email, "password": password}}
    with open("data.json", "r") as password_data:
        passwords = json.load(password_data)
        passwords.update(item)
    
    with open("data.json", "w") as password_data:
        json.dump(passwords, password_data, indent=4)
