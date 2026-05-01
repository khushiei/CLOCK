from tkinter import *
from time import *

def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

def update():
    time_str = strftime("%I:%M:%S %p")
    time_label.config(text=time_str)

    day_str = strftime("%A")
    day_label.config(text=day_str)

    date_str = strftime("%B %d, %Y")
    date_label.config(text=date_str)

    window.after(1000,update)

window = Tk()

window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

window.title("Clock")
icon = PhotoImage(file='time.png')
window.iconphoto(True,icon)
window.config(background="#3E2723")

time_label = Label(window,font=("Arial",50),fg="#F4C9D6",bg="#3E2723",padx=10,pady=60)
time_label.pack()

day_label = Label(window,font=("Arial",25),fg="#F4C9D6",bg="#3E2723")
day_label.pack()

date_label = Label(window,font=("Arial",30),fg="#F4C9D6",bg="#3E2723")
date_label.pack()

photo = PhotoImage(file='kitty.png')
label = Label(window,image=photo,bg="#3E2723")
label.pack()

update()

window.mainloop()