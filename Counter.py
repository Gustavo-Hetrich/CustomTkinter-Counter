import customtkinter as ctk
from tkinter import *
from datetime import datetime
import keyboard

def count():
    given_name = counter_name.get()
    if not given_name.strip():
        no_text = ctk.CTkLabel(window, text = 'Please insert a Title')
        no_text.pack(pady = 2)
        window.after(2000, no_text.destroy)
    else:
        print(given_name)
        # Name of the Counter
        name_place = ctk.CTkLabel(title_place, text= given_name, font = ctk.CTkFont('roboto', size = 15))
        name_place.pack(pady = 5)
        counter_name.delete(0, END)

        # Time that the Button is Pressed
        date = datetime.now()
        current_time = date.strftime('%H:%M:%S')
        timetable = ctk.CTkLabel(time_place, text = current_time, font = ctk.CTkFont('roboto', size = 15))
        timetable.pack(pady = 5)



def key_pressed(enter):
        count()

window = ctk.CTk()
window.title('Counter')
window.geometry('800x700')
window.resizable(False,False)

#title
title = ctk.CTkLabel(window, text= 'Counter', font = ctk.CTkFont('roboto', size = 50))
title.pack(pady = 10)


#Input Field
counter_name = ctk.CTkEntry(window,
placeholder_text= 'Title', 
font = ctk.CTkFont('roboto', size = 15),
width= 200,
height= 50)

counter_name.pack(pady = 30)

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

button.pack(pady = 20)

# Separation Frame 1
title_place = ctk.CTkScrollableFrame(window,
width = 370, height = 370, 
border_color = 'black',)
title_place.place( x = 0, y = 330)


# Separation Frame 2
time_place = ctk.CTkScrollableFrame(window,
width = 370, height = 370,
border_color = 'black')
time_place.place(x = 430, y = 330)

keyboard.on_press_key('Return', key_pressed)

window.mainloop()
