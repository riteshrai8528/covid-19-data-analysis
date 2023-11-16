import tkinter as tk
from tkinter import *
import os
import webbrowser
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("1440x1440")
root.title("COVID-19 TRACKER")
root.iconbitmap(r'virus.ico')
root.configure(background = "sky blue")



frame3=Frame(root,width=350,height=618)
head = PhotoImage(file='world-2.png')
labelphoto = Label(frame3, image = head, )
labelphoto.pack()
label1 = Label(frame3, text = '244,642,470',bg="white",font=('Helvetica', 28, 'bold'))
label1.place(x = 90, y = 170)
label2 = Label(frame3, text = '4,967,316',bg="white",fg="red",font=('Helvetica', 28, 'bold'))
label2.place(x = 90, y = 260)
label2 = Label(frame3, text = '221,641,872',bg="white",fg="light green",font=('Helvetica', 28, 'bold'))
label2.place(x = 90, y = 350)
label2 = Label(frame3, text = '226,609,188',bg="white",font=('Helvetica', 14, 'bold'))
label2.place(x = 50, y = 465)
label2 = Label(frame3, text = '18,033,282',bg="white",font=('Helvetica', 14, 'bold'))
label2.place(x = 233, y = 465)
label2 = Label(frame3, text = '4,967,316',bg="white",fg="red",font=('Helvetica', 14, 'bold'))
label2.place(x = 100, y = 500)
label2 = Label(frame3, text = '221,641,872',bg="white",fg="light green",font=('Helvetica', 14, 'bold'))
label2.place(x = 15 ,y = 500)
label2 = Label(frame3, text = '75,198',bg="white",fg="red",font=('Helvetica', 14, 'bold'))
label2.place(x = 280, y = 500)
label2 = Label(frame3, text = '17,958,084',bg="white",fg="blue",font=('Helvetica', 14, 'bold'))
label2.place(x = 190 ,y = 500)

label2 = Label(frame3, text = 'Data till "26 OCT 2021"',bg="white",font=('Helvetica', 14, 'bold'))
label2.place(x = 170 ,y = 600)
frame3.pack(side=LEFT)

frame4=Frame(root,width=350,height=618)
head1 = PhotoImage(file='indiaa-2.png')
labelphoto = Label(frame4, image = head1, )
labelphoto.pack()
label1 = Label(frame4, text = '34,200,957',bg="white",font=('Helvetica', 28, 'bold'))
label1.place(x = 100, y = 170)
label2 = Label(frame4, text = '455,093',bg="white",fg="red",font=('Helvetica', 28, 'bold'))
label2.place(x = 110, y = 260)
label2 = Label(frame4, text = '33,574,973',bg="white",fg="light green",font=('Helvetica', 28, 'bold'))
label2.place(x = 100, y = 350)
label2 = Label(frame4, text = '34,030,066',bg="white",font=('Helvetica', 14, 'bold'))
label2.place(x = 130, y = 455)

label2 = Label(frame4, text = '455,093',bg="white",font=('Helvetica', 14, 'bold'))
label2.place(x = 180, y = 485)
label2 = Label(frame4, text = '33,574,973',bg="white",fg="light green",font=('Helvetica', 14, 'bold'))
label2.place(x = 95 ,y = 485)
label2 = Label(frame4, text = 'Data till "26 OCT 2021"',bg="white",font=('Helvetica', 14, 'bold'))
label2.place(x = 170 ,y = 600)
frame4.pack(side=RIGHT)





title = Label(root, text="COVID-19 TRACKER", font=("times new roman", 40, "bold"), bg="blue", fg="white",
                     bd=10, relief=GROOVE)
title.place(x=0, y=0, relwidth=1)


photo = PhotoImage(file='India_map-3.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python main.py')
    top.destroy()

    btn1 = Button(top, text="Back").pack()
btn2 = Button(
    root,
    image=photo,
    borderwidth=0,
    compound=CENTER,

    command=open,

)
btn2.pack(pady=(85,10),padx=0)

photo1= PhotoImage(file='button_india.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python main.py')
    top.destroy()

    btn1 = Button(top, text="Back").pack()
btn2 = Button(
    root,
    image=photo1,
    text="'Click Here'",
    compound=TOP,

    command=open,
    borderwidth=0,

    width=0
)
btn2.pack()
def showMsg():
    url= 'file:///Users/mac/Downloads/sidebar-01/index.html'
    webbrowser.open(url, new=2)



button = Button(root,
                text='Submit',
                command=showMsg)
button.pack()




class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'QUIT'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side=BOTTOM)
quitButton(root)



root.mainloop()

