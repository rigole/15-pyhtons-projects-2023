from tkinter import *
from tkinter import messagebox
import urllib
import requests
import json



window = Tk()
API_KEY = '5b7e7dd0b74461ad2133b1bd6d9e2aa0c53a0'

def shorten_function():
    url_to_short = url_input.get()
    #url_shortened_value = url_shortened_label.get()
    key = API_KEY
    url = urllib.parse.quote(url_to_short)
    userDomain = '1'
    if len(url_to_short) == 0:
        messagebox.showinfo(title="Error", message="Please enter an URL")
        
    else:
        response = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(key, url))
        response_json =response.json()
        url_shortened_label.config(text=response_json["url"]["shortLink"])
        
        #print(response_json["url"]["shortLink"])
            




window.title("Url Shortener")
window.minsize(width=500, height=500)

#Welcome text
title_label = Label(text= "Welcome to the URL shortener")
title_label.grid(column=0, row=2, rowspan=2, pady=25)
title_label.config(font=("Courier", 35),justify="center")

#URL ENTRY
url_label = Label(text="Enter URL")
url_label.grid(column=0, row=5, rowspan=1,pady=10)

url_input = Entry(width=75)
url_input.grid(column=0, row=6, rowspan=6, pady=10, ipady=3)

#Button to shorten Link
button_converter = Button(text="Shorten URL", width=25, command=shorten_function)
button_converter.grid(pady=10, column=0, row=18, rowspan=8)

#URL shortened Label
url_shortened_label = Label(text="URL SHORTENED")
url_shortened_label.grid(column=0,row=35,rowspan=8, pady=14)
url_shortened_label.config(font=("Courier", 20), justify="center")


#URL shortened  value
url_shortened_label = Label()
url_shortened_label.grid(column=0,row=55,rowspan=8, pady=14)
window.mainloop()
