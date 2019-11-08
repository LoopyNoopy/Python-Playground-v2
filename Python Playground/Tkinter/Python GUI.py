import tkinter
top = tkinter.Tk("Studio")

top.configure(background = "white")
buttonTest = tkinter.Button(top, text = "This is a button", bg = "blue")

# Code to add widgets will go here...
buttonTest.pack()
top.mainloop()