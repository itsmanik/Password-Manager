import tkinter
import save

windows = tkinter.Tk()
windows.minsize(400, 400)

title_label = tkinter.Label(text="Password Manager", font=(20))
title_label.pack()

platform_label = tkinter.Label(text="Platform: ")
platform_label.pack()
platform = tkinter.Entry()
platform.pack()

email_label = tkinter.Label(text="E-mail: ")
email_label.pack()
email = tkinter.Entry()
email.pack()

password_label = tkinter.Label(text="Password: ")
password_label.pack()
password = tkinter.Entry()
password.pack()

save_button = tkinter.Button(text="Save", command=lambda: save.save(platform.get(), email.get(), password.get()))
save_button.pack()

windows.mainloop()
