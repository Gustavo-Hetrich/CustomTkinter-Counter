import customtkinter as ctk
from tkinter import *
from datetime import datetime
import keyboard

def count():
    given_name = counter_name.get()
    if not given_name.strip():
        no_text = ctk.CTkLabel(window, text = 'Please insert a Title')
        no_text.grid(row = 0, column = 0, sticky = '')
        window.after(2000, no_text.destroy)
    else:
        print(given_name)
        # Name of the Counter
        date = datetime.now()
        name_place = ctk.CTkLabel(title_place, text = given_name + (' ' * 50)  + date.strftime('%H:%M:%S'), font = ctk.CTkFont('roboto', size = 20))
        name_place.pack(pady = 5)
        counter_name.delete(0, END)

def changemode():
    val = appearance.get()
    if val:
         ctk.set_appearance_mode('dark')
    else:
         ctk.set_appearance_mode('light')
    



def key_pressed(enter):
        count()

# Window Configuration
window = ctk.CTk()
window.title('Counter')
window.geometry('800x700')
window.resizable(False,False)

# Grid System
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(0, weight = 1)

#title
title = ctk.CTkLabel(window, text= 'Counter', font = ctk.CTkFont('roboto', size = 40))
title.grid(column = 0, sticky = 'nwe')


# Dark and Light Mode
appearance = ctk.CTkSwitch(window, text = 'Change Mode',
font = ctk.CTkFont('roboto', size = 10),
fg_color = 'purple',
progress_color = 'orange',
onvalue = 0,
offvalue = 1,
command = changemode,)
appearance.grid(row = 0, column = 0, sticky = 's')


#Input Field
counter_name = ctk.CTkEntry(window,
placeholder_text= 'Title', 
font = ctk.CTkFont('roboto', size = 15),
width= 200,
height= 50)

counter_name.grid(row = 0, column = 0, sticky = 'n', pady = 100)

# Confirm Button
button = ctk.CTkButton(
window,
text = "+",
font = ctk.CTkFont('roboto', size = 30),
command = count,
width = 50,
fg_color = 'black',
hover_color = 'purple',
border_width = 2,
border_color = 'black',
corner_radius = 500)

button.grid(row = 0, column = 0, sticky = 'n', pady = 200)

# Separation Frame 1
title_place = ctk.CTkScrollableFrame(window,
width = 370, height = 1000, 
border_color = 'black',)
title_place.grid( row = 0, column = 1, sticky = 'nswe')


keyboard.on_press_key('Return', key_pressed)

window.mainloop()
