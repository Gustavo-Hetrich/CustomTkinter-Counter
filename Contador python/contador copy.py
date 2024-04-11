from tkinter import *

def count():
    print('count')

window = Tk()
window.title('Counter')
window.geometry('700x800')


#title
title = Label(window, text= 'Counter', font = 'roboto 30 bold')
title.pack()

#Input Field
counter_frame = Frame(window)
counter_name = Entry(counter_frame)
button = Button(
counter_frame,
text = "+",
font = 'roboto 20 bold',
command = count)

counter_name.pack(padx = 100)
button.pack(padx = 100)
counter_frame.pack()

window.mainloop()