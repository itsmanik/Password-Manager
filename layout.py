import tkinter

class Layout:

    def __init__(self):
        title_label = tkinter.Label(text="Password Manager", font=(20))
        title_label.pack()

        platform_label = tkinter.Label(text="Platform: ")
        platform_label.pack()
        platform = tkinter.Entry()
        platform.pack()

        password_label = tkinter.Label(text="Password: ")
        password_label.pack()
        password = tkinter.Entry()
        password.pack()

        email_label = tkinter.Label(text="E-mail: ")
        email_label.pack()
        email = tkinter.Entry()
        email.pack()

        save_button = tkinter.Button(text="Save")
        save_button.pack()