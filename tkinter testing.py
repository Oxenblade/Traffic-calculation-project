from tkinter import *

# label creating
'''root = Tk()

mylabel = Label(root, text= "Hello World")

mylabel.pack()

root.mainloop()'''

#button and label creating 
'''root = Tk()


def my_Click():
    my_label = Label(root, text = " Hey Yo ! I clicked a button !", fg = "Brown", bg = "Light Green")
    my_label.pack()


my_button = Button(root, text= "Click Me Dammit! ", command =my_Click, fg= "Red", bg ="Yellow")
my_button.pack()

root.mainloop()'''

#input fields

'''root = Tk()

e = Entry(root, width=50, borderwidth=15)
e.pack()
e.insert(0, "Enter your name: ")

def my_Click():
    Hello = "Hello" + e.get()
    my_label = Label(root, text= Hello)
    my_label.pack()


my_button = Button(root, text= "Click Me Dammit! ", command =my_Click, fg= "Red", bg ="Yellow")
my_button.pack()

root.mainloop()'''


root = Tk()

e = Entry(root, width=50, borderwidth=15)
e.pack()
e.insert(0, "Enter your name: ")

def my_Click():
    Hello = "Hello" + e.get()
    my_label = Label(root, text= Hello)
    my_label.pack()


my_button = Button(root, text= "Click Me Dammit! ", command =my_Click, fg= "Red", bg ="Yellow")
my_button.pack()

root.mainloop()
