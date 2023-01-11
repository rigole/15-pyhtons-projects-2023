from tkinter import *
from tkinter import messagebox

window = Tk()


def shorten_function():
    url_to_short = url_input.get()
    
    if len(url_to_short) == 0:
        messagebox.showinfo(title="Error", message="Please enter an URL")









window.title("Url Shortener")
window.minsize(width=500, height=500)

title_label = Label(text= "Welcome to the URL shortener")
title_label.grid(column=0, row=2, rowspan=2, pady=25)
title_label.config(font=("Courier", 35),justify="center")

url_label = Label(text="Enter URL")
url_label.grid(column=0, row=5, rowspan=1,pady=10)

url_input = Entry(width=75)
url_input.grid(column=0, row=6, rowspan=6, pady=10, ipady=3)

button_converter = Button(text="Shorten URL", width=25, command=shorten_function)
button_converter.grid(pady=10, column=0, row=18, rowspan=8)




window.mainloop()
