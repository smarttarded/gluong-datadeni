import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
import os, stat
from tkinter.constants import X
import subprocess
from cryptography.fernet import Fernet
#MADE BY [khiem g luong].

root = tk.Tk()
root.title("DATADENI")

root.geometry("500x350")
root.eval('tk::PlaceWindow . center')

root.minsize(300, 350)
root.maxsize(300, 350)

root.iconbitmap('favicon.ico')

bg_img = tk.PhotoImage(file="matrix.gif")
imglabel = tk.Label(root, image=bg_img)

frameCnt = 27
frames = [PhotoImage(file='matrix.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

#def update(ind):
#     frame = frames[ind]
#     ind += 1
#     if ind == frameCnt:
#         ind = 0
#     imglabel.configure(image=frame)
#     root.after(100, update, ind)
# imglabel = Label(root)
# imglabel.place(height=800, width=230,rely=-.6)
# root.after(0, update, 0)

key = Fernet.generate_key()

with open('mykey.key', 'ab') as mykey:
    mykey.write(key + b'\n')

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)

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
    arr = os.walk(selection)
    for dirname, dirnames, filenames in arr:
    # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
    # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))

open("logins.txt", "a")
subprocess.check_call(["attrib","+H","logins.txt"])

def hideFolder():
    secFolder = folders.get()
    namer = open("logins.txt", "r")
    readfile = namer.read()
    password = E1.get()
    if(f'{password}' == ''):
        showinfo("DATADENI", "you must create a password.")
        return
    # elif (f'{password}' == '') and f'{secFolder}' in readfile:
    #      for files in os.listdir(f'{secFolder}'):
    #         print("checkFolder " + files)
    #         os.system("attrib +h " + files)   
    #     os.system("attrib +h " + f'{secFolder}')       
    elif f'{password}' and f'{secFolder}' in readfile:
        showinfo("DATADENI", "this password or folder is already registered.") 
        for files in os.listdir(f'{secFolder}'):
            print("checkFolder " + files)
            os.system("attrib +h " + files)   
        os.system("attrib +h " + f'{secFolder}')
    else:
        for files in os.listdir(f'{secFolder}'):
            print("checkFolder " + files)
            os.system("attrib +h " + files)
        open("logins.txt", "a").write(password + ' ' + secFolder + '\n') 
        os.system("attrib +h " + f'{secFolder}')
        E1.delete(0, 'end')

def unhideFolder():
    password2 = E2.get()
    secFolder2 = folders.get()
    namer = open("logins.txt", "r")
    readfile = namer.read()
    if(password2 == 'pluriselect'):
        os.system("attrib -h " + f'{secFolder2}') 
        subprocess.check_call(["attrib","-H","logins.txt"])
    elif f'{password2}' and f'{secFolder2}' in readfile:
        os.system("attrib -h " + f'{secFolder2}')
        for files in os.listdir(f'{secFolder2}'):
            print("checkFolder " + files)
            os.system("attrib -h " + files)

    else:
        showinfo("DATADENI", "the password for this folder didn't match.") 
    E2.delete(0, 'end')

def decryptFolder():
    fernet = Fernet(key)
    secFolder = folders.get()
    arr = os.walk(f'{secFolder}')
    for dirname, dirnames, filenames in arr:
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
    for filename in filenames:
        print(os.path.join(dirname, filename))
        f = open(os.path.join(dirname, filename), 'rb')
        original = f.read()
        print(original)
        # with open (files, 'wb') as encrypted_file:
        decrypted = fernet.decrypt(original)
        with open(os.path.join(dirname, filename), 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

def encryptFolder():
    fernet = Fernet(key)
    secFolder = folders.get()
    arr = os.walk(f'{secFolder}')
    for dirname, dirnames, filenames in arr:
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
    for filename in filenames:
        print(os.path.join(dirname, filename))
        f = open(os.path.join(dirname, filename), 'rb')
        original = f.read()
        print(original)
        # with open (files, 'wb') as encrypted_file:
        encrypted = fernet.encrypt(original)
        with open(os.path.join(dirname, filename), 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

folders = StringVar(root)
folders.set(dirArray[0]) # default value

dirArrayList = list(dirArray)
print(dirArrayList)



L1 = tk.Label(root, borderwidth=2, relief='sunken', text="choose a folder")
L1.pack(padx=20, pady=5)

OM1 = tk.OptionMenu(root, folders, *dirArrayList, command=callback)
OM1.pack(padx=20, pady=10)

L1 = tk.Label(root, borderwidth=2, relief='sunken', text="create password")
L1.pack(padx=20, pady=5)
E1 = tk.Entry(root, bd =2)
E1.pack(padx=20, pady=5)

var1 = IntVar()
Chk1 = tk.Button(root, text="HIDE",padx=10, pady=5, command=hideFolder)
Chk1.pack()

var1n = IntVar()
Chk1n = tk.Button(root, text="ENCRYPT",padx=10, pady=5, command=encryptFolder)
Chk1n.pack()

L2 = tk.Label(root, borderwidth=2, relief='sunken', text="enter password")
L2.pack(padx=20, pady=5)
E2 = tk.Entry(root, bd =2)
E2.pack(padx=20, pady=5)

Chk2 = tk.Button(root, text="UNHIDE",padx=10, pady=5, command=unhideFolder)
Chk2.pack()

Chk3 = tk.Button(root, text="DECRYPT",padx=10, pady=5, command=decryptFolder)
Chk3.pack()

def on_closing():
    subprocess.check_call(["attrib","+H","logins.txt"])
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
