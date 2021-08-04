'''Tkinter cheatsheet'''

# importing the tkinter library
from tkinter import *

# the root window
root = Tk()

# title of the window
root.title("Tkinter Window")

# size of the window
root.geometry("800x600")

# frame
myFrame = Frame(root, bg="blue", height=200, width=500)

# placing the frame of the window
myFrame.place(x=150, y=50)

# lable
frameLable = Label(myFrame, text="I am dancing on a frame", font=("Sans", 18), fg="blue")
frameLable.pack(side="right")

# lable
myLable = Label(root, text="Hello world", bg="blue", fg="white")
myLable.place(x=10, y=50)

#buttons
myButton = Button(root, text="Click Me", height=3, width=12, bg="blue", fg="white")
myButton.place(x=10, y=200)

# entry point
myEntry = Entry(root, font=("Sans", 14))
myEntry.place(x=10, y=300)



if __name__ == "__main__":
    root.mainloop()