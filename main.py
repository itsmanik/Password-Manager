import tkinter
import save

window = tkinter.Tk()
window.title("Password Manager")
logo = tkinter.PhotoImage(file="logo.png")
window.iconphoto(False, logo)
window.config(bg="#E1E9EF", padx=100, pady=50)

title_label = tkinter.Label(text="Password Manager", font=("", 25, "bold"), fg="#161616", bg="#E1E9EF")
title_label.grid(row=1, column=1, columnspan=2, pady=(0, 40))

platform_label = tkinter.Label(text="Platform", bg="#E1E9EF", font=("", 12, "normal")) 
platform_label.grid(row=2, column=1, sticky="W")
platform = tkinter.Entry(font=("", 15, "normal"))
platform.grid(row=3, column=1, pady=(0, 20), padx=(0, 50))

email_label = tkinter.Label(text="E-mail", bg="#E1E9EF", font=("", 12, "normal"))
email_label.grid(row=2, column=2, sticky="w")
email = tkinter.Entry(font=("", 15, "normal"))
email.grid(row=3, column=2, pady=(0, 20))

password_label = tkinter.Label(text="Password", bg="#E1E9EF", font=("", 12, "normal"))
password_label.grid(row=4, column=1, sticky="W")
password = tkinter.Entry(font=("", 15, "normal"))
password.grid(row=5, column=1, pady=(0, 12), padx=(0, 50))

save_button = tkinter.Button(text="Save", command=lambda: save.save(platform, email, password), fg="white", bg="#4D7044", font=("", 12, "normal"))
save_button.grid(row=5, column=2, sticky="ewn")

canvas = tkinter.Canvas(width=500, height=70, bg="#E1E9EF", highlightthickness=0)
canvas.create_line(0, 35, 500, 35, width=2, fill="#6C6C6C")
canvas.grid(row=6, column=1, columnspan=2)

load_platform_label = tkinter.Label(text="Platform", bg="#E1E9EF", font=("", 12, "normal"))
load_platform_label.grid(row=7, column=1, sticky="w")
load_platform_entry = tkinter.Entry(font=("", 15, "normal"))
load_platform_entry.grid(row=8, column=1, pady=(0, 20), padx=(0, 50))

load_button = tkinter.Button(text="Load", fg="white", bg="#54859B", font=("", 12, "normal"), padx=50)
load_button.grid(row=8, column=2, sticky="nw")

window.mainloop()
