import customtkinter as ctk
from tkinter import *
from datetime import datetime
import keyboard


# List Counter
counter = 1
# New timestamps
list_one = ['list1',]
# Repeated timestamps
list_two = ['list2',]

def count():

    global counter
    given_name = timestamp_name.get()
    timestamp = given_name
    
    # If the input entry is empty
    if not given_name.strip():
        no_text = ctk.CTkLabel(window, text='Please insert a Title')
        no_text.grid(row=0, column=0, sticky='n', pady = 285)
        window.after(2000, no_text.destroy)

    # If already exist
    else:
        if given_name in list_one:
            timestamp = given_name + (' ') + str(counter)
            list_two.append(timestamp)
            print(list_two)
            counter += 1
            print(counter)
        elif timestamp in list_two:
            timestamp = given_name + (' ') + str(counter)
            list_two.append(timestamp)
            print(list_two)
            counter += 1
            print(counter)
        else:
            timestamp = given_name
            list_one.append(given_name)
            print(list_one)
        
        # Name of the timestamp
        date = datetime.now()
        time_of_press = date.strftime('%Hh %Mm %Ss')
        title_place = ctk.CTkLabel(title_frame, text=timestamp, pady=10, font=ctk.CTkFont('helvetica', size=20))
        title_place.pack(anchor='n', side='bottom')
        time_place = ctk.CTkLabel(time_frame, text=time_of_press, pady=10, font=ctk.CTkFont('helvetica', size=20))
        time_place.pack(anchor='n', side='bottom')
        timestamp_name.delete(0, END)

def clear():
    global counter
    for widget in title_frame.winfo_children():
        widget.destroy()
    for widget in time_frame.winfo_children():
        widget.destroy()
    list_one.clear()
    list_two.clear()
    counter = 1
    cleared = ctk.CTkLabel(window, text = 'Timestamps Cleared')
    cleared.grid(row=0, column=0, sticky='n', pady=285)
    window.after(2000, cleared.destroy)

# Script for changing themes
color = ['orange', 'purple']

def changemode():
    val = appearance.get()
    if val:
        ctk.set_appearance_mode('dark')
        color[1]
    else:
        ctk.set_appearance_mode('light')
        color[0]

def key_pressed(enter):
    count()

# Window Configuration
window = ctk.CTk()
window.title('TimeStamper')
window.geometry('800x700')

# Grid System
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.rowconfigure(0, weight=1)

# Title
title = ctk.CTkLabel(window, text='TimeStamper', 
font=ctk.CTkFont('helvetica', size=39),
fg_color=color,
pady=20)

title.grid(column=0, sticky='nwe')

# Dark and Light Mode
appearance = ctk.CTkSwitch(window, text='Change Theme',
font=ctk.CTkFont('helvetica', size=15),
fg_color='purple',
progress_color='orange',
height=50,
onvalue=0,
offvalue=1,
command=changemode)

appearance.grid(row=0, column=0, sticky='s', padx = 5)

# Input Field
timestamp_name = ctk.CTkEntry(window, placeholder_text='Title',
font=ctk.CTkFont('helvetica',
size=15),
width=200,
height=50,
corner_radius=500)

timestamp_name.grid(row=0, column=0, sticky='n', pady=150, padx=5)

# Confirm Button
button = ctk.CTkButton(window, text="+",
font=ctk.CTkFont('helvetica', size=30),
command=count,
width=50,
fg_color=color,
hover_color=color,
border_width=2,
border_color='black',
corner_radius=500)

button.grid(row=0, column=0, sticky='n', pady=205, padx = 5)

# Clear result Button
clear_result = ctk.CTkButton(window, text="clear",
font=ctk.CTkFont('helvetica', size=25),
command=clear,
fg_color='black',
hover_color=color,
border_width=2,
border_color='black',
corner_radius=20)

clear_result.grid(row=0, column=0, sticky='n', pady=250, padx = 5)

# Credits
credits = ctk.CTkLabel(window, text = 'Made By: Gustavo Hetrich',
font=ctk.CTkFont('helvetica', size = 10))

credits.grid(row=1, column=0, sticky = 'n', padx = 5)

# Result Frame
result = ctk.CTkScrollableFrame(window,
width=370,
height=1000,
border_color='black',)

result.grid(row=0, column=1, sticky='nswe')

# column in the frame (title and time)
result.columnconfigure(0, weight=1)
result.columnconfigure(1, weight=1)

# Title Frame
title_frame = ctk.CTkFrame(result,
width=(370/2),
height=1000)

title_frame.grid(row=0, column=0, sticky='n')

# Time Frame
time_frame = ctk.CTkFrame(result,
width=(370/2),
height=1000)

time_frame.grid(row=0, column=1, sticky='n')

keyboard.on_press_key('Return', key_pressed)

window.mainloop()
