import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
import os, stat
from tkinter.constants import X
import subprocess

#MADE BY [khiem g luong].

root = tk.Tk()
root.title("DATADENI")

root.geometry("500x350")
root.eval('tk::PlaceWindow . center')

root.minsize(230, 350)
root.maxsize(230, 350)

root.iconbitmap('favicon.ico')

bg_img = tk.PhotoImage(file="matrix.gif")
imglabel = tk.Label(root, image=bg_img)

frameCnt = 27
frames = [PhotoImage(file='matrix.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    imglabel.configure(image=frame)
    root.after(100, update, ind)
imglabel = Label(root)
imglabel.place(height=800, width=230,rely=-.6)
root.after(0, update, 0)

path = '.'
dirArray = []

def isPython(versionNumber): # Check the version of python running
    import platform
    return platform.python_version().startswith(str(versionNumber))

def consoleReadLine(message): # Read a string from the console
    if isPython(3): # Python 3.x code
        return input(message)


directory_contents = os.listdir(path)
for item in directory_contents:
    if os.path.isdir(item):
        print(item)
        dirArray.append(item)


def callback(selection):
    arr = os.listdir(selection)
    print(arr)

open("logins.txt", "a")
subprocess.check_call(["attrib","+H","logins.txt"])

def checkFolder():
    secFolder = folders.get()
    namer = open("logins.txt", "r")
    readfile = namer.read()
    password = E1.get()
    if(f'{password}' == ''):
        showinfo("DATADENI", "you must create a password.")
        return
    if f'{password}' and f'{secFolder}' in readfile:
        showinfo("DATADENI", "this password or folder is already registered.")    
    else:
        for files in os.listdir(f'{secFolder}'):
            print("checkFolder " + files)

        open("logins.txt", "a").write(password + ' ' + secFolder + '\n') 
        os.system("attrib +h " + f'{secFolder}')
        E1.delete(0, 'end')

def revealFolder():
    password2 = E2.get()
    secFolder2 = folders.get()
    namer = open("logins.txt", "r")
    readfile = namer.read()
    if(password2 == 'admin'):
        os.system("attrib -h " + f'{secFolder2}') 
        subprocess.check_call(["attrib","-H","logins.txt"])
    elif f'{password2}' and f'{secFolder2}' in readfile:
        os.system("attrib -h " + f'{secFolder2}')
    else:
        showinfo("DATADENI", "the password for this folder didn't match.") 
    E2.delete(0, 'end')

def secureFolder():
    secFolder3 = folders.get()
    os.system("attrib +h " + f'{secFolder3}')
    subprocess.check_call(["attrib","+H","logins.txt"])


folders = StringVar(root)
folders.set(dirArray[0]) # default value

dirArrayList = list(dirArray)
print(dirArrayList)



L1 = tk.Label(root, borderwidth=2, relief='sunken', text="choose a folder")
L1.pack(padx=20, pady=10)

OM1 = tk.OptionMenu(root, folders, *dirArrayList, command=callback)
OM1.pack(padx=20, pady=10)

L1 = tk.Label(root, borderwidth=2, relief='sunken', text="create password")
L1.pack(padx=20, pady=10)
E1 = tk.Entry(root, bd =2)
E1.pack(padx=20, pady=5)

var1 = IntVar()
Chk1 = tk.Button(root, text="SECURE",padx=10, pady=5, command=checkFolder)
Chk1.pack()

L2 = tk.Label(root, borderwidth=2, relief='sunken', text="enter password")
L2.pack(padx=20, pady=10)
E2 = tk.Entry(root, bd =2)
E2.pack(padx=20, pady=5)

Chk2 = tk.Button(root, text="REVEAL",padx=10, pady=5, command=revealFolder)
Chk2.pack()

Chk3 = tk.Button(root, text="RESECURE",padx=10, pady=5, command=secureFolder)
Chk3.pack()

def on_closing():
    subprocess.check_call(["attrib","+H","logins.txt"])
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
