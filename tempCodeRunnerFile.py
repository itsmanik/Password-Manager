import tkinter
import save
import load

window = tkinter.Tk()
window.title("Password Manager")
logo = tkinter.PhotoImage(file="logo.png")
window.iconphoto(False, logo)
window.config(bg="#E1E9EF", padx=100, pady=50)

# Header
title_label = tkinter.Label(text="Password Manager", font=("", 25, "bold"), fg="#161616", bg="#E1E9EF")
title_label.grid(row=1, column=1, columnspan=2, pady=(0, 40))

# Platform
platform_label = tkinter.Label(text="Platform", bg="#E1E9EF", font=("", 12, "normal")) 
platform_label.grid(row=2, column=1, sticky="W")
platform = tkinter.Entry(font=("", 15, "normal"))
platform.grid(row=3, column=1, pady=(0, 20), padx=(0, 50))

# Username
username_label = tkinter.Label(text="Username", bg="#E1E9EF", font=("", 12, "normal")) 
username_label.grid(row=2, column=2, sticky="W", columnspan=2)
username = tkinter.Entry(font=("", 15, "normal"))
username.grid(row=3, column=2, pady=(0, 20), padx=(0, 50), columnspan=2)

# Phone Number
phone_number_label = tkinter.Label(text="Phone Number", bg="#E1E9EF", font=("", 12, "normal")) 
phone_number_label.grid(row=4, column=1, sticky="W")
phone_number = tkinter.Entry(font=("", 15, "normal"))
phone_number.grid(row=5, column=1, pady=(0, 20), padx=(0, 50))

# Password
password_label = tkinter.Label(text="Password", bg="#E1E9EF", font=("", 12, "normal"))
password_label.grid(row=4, column=2, sticky="W", columnspan=2)
password = tkinter.Entry(font=("", 15, "normal"))
password.grid(row=5, column=2, pady=(0, 12), padx=(0, 50), columnspan=2)

# E-Mail
email_label = tkinter.Label(text="E-mail", bg="#E1E9EF", font=("", 12, "normal"))
email_label.grid(row=6, column=1, sticky="w")
email = tkinter.Entry(font=("", 15, "normal"))
email.grid(row=7, column=1, pady=(0, 12), padx=(0, 50))

# Save Button
save_button = tkinter.Button(text="Save", command=lambda: save.save(platform, username, phone_number, email, password), fg="white", bg="#1C7007", font=("", 12, "normal"))
save_button.grid(row=7, column=2, sticky="ewn", pady=(0, 12), padx=(0, 50), columnspan=2)

# Horizontal Line
canvas = tkinter.Canvas(width=750, height=70, bg="#E1E9EF", highlightthickness=0)
canvas.create_line(0, 35, 750, 35, width=2, fill="grey")
canvas.grid(row=8, column=1, columnspan=3, sticky="ew")

# Load
load_platform_label = tkinter.Label(text="Platform", bg="#E1E9EF", font=("", 12, "normal"))
load_platform_label.grid(row=9, column=1, sticky="w")
load_platform = tkinter.Entry(font=("", 15, "normal"))
load_platform.grid(row=10, column=1, pady=(0, 20), padx=(0, 50))

# Load Button
load_button = tkinter.Button(text="Load", fg="white", bg="#10688E", width=8, padx=10, font=("", 12, "normal"), command=lambda: load.load(load_platform, window))
load_button.grid(row=10, column=2, sticky="ew")
