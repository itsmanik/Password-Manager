import json
import tkinter
import tkinter.messagebox

def load(platform, window):
    platform_text = platform.get()
    platform.delete(0, "end")


    try:
        with open("data.json") as data:
            saved_passwords = json.load(data)
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="Error", message="You need to save some information before accessing!")
        return

    try:
        saved_passwords[platform_text]
    except KeyError:
        tkinter.messagebox.showerror(title="Error", message="The information you are trying to find, does not exists!")
        return

    mail = saved_passwords[platform_text]["email"]
    password = saved_passwords[platform_text]["password"]
    username = saved_passwords[platform_text]["username"]
    phone_number = saved_passwords[platform_text]["phone_number"]
    
    
    show_info_window = tkinter.Toplevel(window)
    show_info_window.title("Saved")
    logo = tkinter.PhotoImage(file="logo.png")
    show_info_window.iconphoto(False, logo)
    show_info_window.config(bg="#E1E9EF", padx=70, pady=30)

    # Header
    heading_label = tkinter.Label(show_info_window, text="Your Saved Details", font=("", 15, "underline", "bold"), fg="#161616", bg="#E1E9EF")
    heading_label.grid(column=1, row=1, columnspan=2, pady=(0, 20))

    # Platform
    platform_label = tkinter.Label(show_info_window, text="Platform: ", bg="#E1E9EF", font=("", 12, "normal")) 
    platform_label.grid(row=2, column=1, sticky="W")
    platform_saved = tkinter.Label(show_info_window, text=platform_text, bg="#E1E9EF", font=("", 12, "normal")) 
    platform_saved.grid(row=2, column=2, sticky="W")

    # E-Mail
    email_label = tkinter.Label(show_info_window, text="E-Mail: ", bg="#E1E9EF", font=("", 12, "normal")) 
    email_label.grid(row=3, column=1, sticky="W")
    email_saved = tkinter.Label(show_info_window, text=mail, bg="#E1E9EF", font=("", 12, "normal")) 
    email_saved.grid(row=3, column=2, sticky="W")

    # Phone Number
    phone_number_label = tkinter.Label(show_info_window, text="Phone Number: ", bg="#E1E9EF", font=("", 12, "normal")) 
    phone_number_label.grid(row=4, column=1, sticky="W")
    phone_number_saved = tkinter.Label(show_info_window, text=phone_number, bg="#E1E9EF", font=("", 12, "normal")) 
    phone_number_saved.grid(row=4, column=2, sticky="W")

    # Username
    username_label = tkinter.Label(show_info_window, text="Username: ", bg="#E1E9EF", font=("", 12, "normal")) 
    username_label.grid(row=5, column=1, sticky="W")
    username_saved = tkinter.Label(show_info_window, text=username, bg="#E1E9EF", font=("", 12, "normal")) 
    username_saved.grid(row=5, column=2, sticky="W")

    # Password
    password_label = tkinter.Label(show_info_window, text="Password: ", bg="#E1E9EF", font=("", 12, "normal")) 
    password_label.grid(row=6, column=1, sticky="W")
    password_saved = tkinter.Label(show_info_window, text=password, bg="#E1E9EF", font=("", 12, "normal")) 
    password_saved.grid(row=6, column=2, sticky="W")
