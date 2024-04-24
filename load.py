import json
import tkinter

def load(platform, window):
    platform_text = platform.get()
    platform.delete(0, "end")

    with open("data.json") as data:
        print(json.load(data))
    
    show_info_window = tkinter.Toplevel(window)
    show_info_window.title("Saved")
    logo = tkinter.PhotoImage(file="logo.png")
    # show_info_window.minsize(height=350, width=700)
    show_info_window.iconphoto(False, logo)
    show_info_window.config(bg="#E1E9EF", padx=70, pady=30)

    heading_label = tkinter.Label(show_info_window, text="Your Saved Details", font=("", 15, "underline", "bold"), fg="#161616", bg="#E1E9EF")
    heading_label.grid(column=1, row=1, columnspan=2, pady=(0, 20))

    platform_label = tkinter.Label(show_info_window, text="Platform: ", bg="#E1E9EF", font=("", 12, "normal")) 
    platform_label.grid(row=2, column=1, sticky="W")
    platform_saved = tkinter.Label(show_info_window, text="Instagram", bg="#E1E9EF", font=("", 12, "normal")) 
    platform_saved.grid(row=2, column=2, sticky="W")

    email_label = tkinter.Label(show_info_window, text="E-Mail: ", bg="#E1E9EF", font=("", 12, "normal")) 
    email_label.grid(row=3, column=1, sticky="W")
    email_saved = tkinter.Label(show_info_window, text="maniksh2004@gmail.com", bg="#E1E9EF", font=("", 12, "normal")) 
    email_saved.grid(row=3, column=2, sticky="W")

    password_label = tkinter.Label(show_info_window, text="Password: ", bg="#E1E9EF", font=("", 12, "normal")) 
    password_label.grid(row=4, column=1, sticky="W")
    password_saved = tkinter.Label(show_info_window, text="password12345", bg="#E1E9EF", font=("", 12, "normal")) 
    password_saved.grid(row=4, column=2, sticky="W")
