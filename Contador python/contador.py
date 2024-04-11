from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def count():
    messagebox.askquestion(image)

window = Tk()
window.title('Calculadora')
window.geometry('700x800')


#title
title = Label(window, text= 'Favor insira o calculo', font = 'roboto 30 bold')
title.pack()

#Input Field
counter_frame = Frame(window)
counter_name = Entry(counter_frame)
button = Button(
counter_frame,
text = "Calcular",
font = 'roboto 20 bold',
command = count)

counter_name.pack()
button.pack()
counter_frame.pack()

idk = Image.open('/home/gustavo/Desktop/Projetos Code/test.png').resize((400,400))
image_tk = ImageTk.PhotoImage(idk)

image = Label(window, image = image_tk)
image.pack()

window.mainloop()