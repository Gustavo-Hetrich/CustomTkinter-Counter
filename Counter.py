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
        time_of_press = date.strftime('%H:%M:%S')
        title_place = ctk.CTkLabel(title_frame,text = given_name, pady = 10, font = ctk.CTkFont('roboto', size = 20))
        title_place.pack(anchor = 'n', side = 'top')
        time_place = ctk.CTkLabel(time_frame,text = time_of_press, pady = 10, font = ctk.CTkFont('roboto', size = 20))
        time_place.pack(anchor = 'n', side = 'top')
        counter_name.delete(0, END)

def clear():
    for widget in title_frame.winfo_children():
            widget.destroy()
    for widget in time_frame.winfo_children():
            widget.destroy()

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

# Grid System
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(0, weight = 1)

#title
title = ctk.CTkLabel(window, text= 'Counter', font = ctk.CTkFont('roboto', size = 40))
title.grid(column = 0, sticky = 'nwe')


# Dark and Light Mode
appearance = ctk.CTkSwitch(window, text = 'Change Theme',
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

# Clear result Button
clear_result = ctk.CTkButton(
window,
text = "Clear",
font = ctk.CTkFont('roboto', size = 30),
command = clear,
width = 50,
fg_color = 'black',
hover_color = 'purple',
border_width = 2,
border_color = 'black',
corner_radius = 500)

clear_result.grid(row = 0, column = 0, sticky = 'n', pady = 260)

# Result Frame
result = ctk.CTkScrollableFrame(window,
width = 370, height = 1000, 
border_color = 'black',)
result.grid( row = 0, column = 1, sticky = 'nswe')

#column in the frame (title and time)
result.columnconfigure(0, weight = 1)
result.columnconfigure(1, weight = 1)

# Title Frame
title_frame = ctk.CTkFrame(result, width = (370/2), height = 1000)
title_frame.grid(row =0, column = 0, sticky = 'n')
title_frame.propagate(False)
# Time Frame
time_frame = ctk.CTkFrame(result, width = (370/2),  height = 1000)
time_frame.grid(row =0, column = 1, sticky = 'n')
time_frame.propagate(False)

keyboard.on_press_key('Return', key_pressed)

window.mainloop()
