from tkinter import *

root = Tk()    

users = [['Anne', 'password1', ['friend1', 'friend2', 'friend3']], ['Bea', 'password2', ['friend1', 'friend2', 'friend3']], ['Chris', 'password1', ['friend1', 'friend2', 'friend3']]]

def showYourself():
    print(users.get())
    return()

for x in range(len(users)):
    l = Checkbutton(root, text=users[x][0], variable=users[x], command = showYourself)
    print ("l = Checkbutton(root, text=" + str(users[x][0]) + ", variable=" + str(users[x]))
    l.pack(anchor = 'w')

root.mainloop()

