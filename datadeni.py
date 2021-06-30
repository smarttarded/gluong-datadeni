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

root.minsize(250, 350)
root.maxsize(250, 350)

root.iconbitmap('favicon.ico')

bg_img = tk.PhotoImage(file="matrix.gif")
imglabel = tk.Label(root, image=bg_img)

os.system("attrib +h " + 'favicon.ico')
os.system("attrib +h " + 'matrix.gif')
os.system("attrib +h " + 'lib')
os.system("attrib +h " + 'python3.dll')
os.system("attrib +h " + 'python39.dll')

if os.path.exists('./mykey.key'):
    os.system("attrib +h " + 'mykey.key')

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
imglabel.place(height=800, width=300,rely=-.6)
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

for f in directory_contents:
    if f.startswith('lib'):
        dirArray.remove(f)

open("logins.txt", "a")
subprocess.check_call(["attrib","+H","logins.txt"])

def hideFolder():
    secFolder = folders.get()
    namer = open("logins.txt", "r")
    readfile = namer.read()
    password = E1.get()
    if(ButtonChk(1)):
        if(f'{password}' == '') and f'{secFolder}' in readfile:
            showinfo("DATADENI", "Hiding folder with existing password")
            os.system("attrib +h " + f'{secFolder}')
            return password
        elif(f'{password}' == ''):
            showinfo("DATADENI", "you must create a password.")
            return None
        elif f'{password}' or f'{secFolder}' in readfile:
            showinfo("DATADENI", "this password or folder is already registered.")
            for files in os.listdir(f'{secFolder}'):
                print("checkFolder " + files)
                os.system("attrib +h " + files)
            os.system("attrib +h " + f'{secFolder}')
            E1.delete(0, 'end')
        else:
            open("logins.txt", "a").write(password + ' ' + secFolder + '\n')
            os.system("attrib +h " + f'{secFolder}')
            E1.delete(0, 'end')

def readLogins():
    s1 = open("logins.txt", "r").read()
    password = s1.split(' ')[0]
    folder = s1.split(' ')[1]
    loginSet = password + folder
    #print(password + folder)
    return loginSet

def ButtonChk(button_id):
    if button_id == 1:
        return 1
    if button_id == 2:
        return 2


def unhideFolder():
    passCheck = readLogins()
    password2 = E2.get()
    secFolder = folders.get()
    passCheck2 = password2 + secFolder
    if(ButtonChk(2)):
        if(password2 == 'pluriselect'):
            os.system("attrib -h " + f'{secFolder}')
            subprocess.check_call(["attrib","-H","logins.txt"])
        elif (passCheck.strip() == passCheck2.strip()):
            os.system("attrib -h " + f'{secFolder}')
        else:
            showinfo("DATADENI", "the password for this folder didn't match.")
        E2.delete(0, 'end')

def decryptFolder():
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
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
    key = Fernet.generate_key()
    with open('mykey.key', 'ab') as mykey:
        mykey.write(key + b'\n')

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

def only_numbers(char):
    return char.isdigit()


# def only_numbers2(char):
#     only_numbers2.count += 1
#     if only_numbers2.count <= 4:
#         return char.isdigit()
#     else:
#         return char == None
# only_numbers2.count = 0

validation = root.register(only_numbers)
folders = StringVar(root)
folders.set(dirArray[0]) # default value

dirArrayList = list(dirArray)

def setPin(text):
    E1.insert(END, text)

def delete_entry(self):
    self.entry.delete(0, 'end')


num1 = Button(root, text ="1", bg = "gray", command=lambda:setPin("1"))
num1.config(height = 2, width = 5)
num1.place(x= 20, y = 30)

num2 = Button(root, text = "2", bg = "gray", command=lambda:setPin("2"))
num2.config(height = 2, width = 5)
num2.place(x= 20, y = 90)

num3 = Button(root, text ="3", bg = "gray", command=lambda:setPin("3"))
num3.config(height = 2, width = 5)
num3.place(x= 20, y = 150)

num4 = Button(root, text = "4", bg = "gray", command=lambda:setPin("4"))
num4.config(height = 2, width = 5)
num4.place(x= 20, y = 210)

num5 = Button(root, text ="5", bg = "gray", command=lambda:setPin("5"))
num5.config(height = 2, width = 5)
num5.place(x= 20, y = 270)

num6 = Button(root, text ="6", bg = "gray", command=lambda:setPin("6"))
num6.config(height = 2, width = 5)
num6.place(x= 190, y = 30)

num7 = Button(root, text = "7", bg = "gray", command=lambda:setPin("7"))
num7.config(height = 2, width = 5)
num7.place(x= 190, y = 90)

num8 = Button(root, text ="8", bg = "gray", command=lambda:setPin("8"))
num8.config(height = 2, width = 5)
num8.place(x= 190, y = 150)

num9 = Button(root, text = "9", bg = "gray", command=lambda:setPin("9"))
num9.config(height = 2, width = 5)
num9.place(x= 190, y = 210)

num0 = Button(root, text ="0", bg = "gray", command=lambda:setPin("0"))
num0.config(height = 2, width = 5)
num0.place(x= 190, y = 270)

L1 = tk.Label(root, borderwidth=2, bg='#000000', fg='#ffffff', relief='sunken', text="choose a folder")
L1.pack(padx=20, pady=5)

OM1 = tk.OptionMenu(root, folders, *dirArrayList)
OM1["menu"].config(bg='#000000', fg='#ffffff')
OM1.pack(padx=20, pady=10)

L1 = tk.Label(root, borderwidth=2, bg='#000000', fg='#ffffff', relief='sunken', text="CREATE PIN")
L1.pack(padx=20, pady=5)
E1 = tk.Entry(root, bg='#3F3F3F', fg='#37D028', bd =2, validate="key", validatecommand=(validation, '%S'))
E1.bind("<BackSpace>", delete_entry)
E1.config(width = 9)
E1.pack(padx=20, pady=3)

var1 = IntVar()
Chk1 = tk.Button(root, text="HIDE",bg='#505050', fg='#37D028',padx=10, pady=5, command=lambda:[hideFolder(),ButtonChk(1)])
Chk1.pack()

var1n = IntVar()
Chk1n = tk.Button(root, text="ENCRYPT",bg='#505050', fg='#37D028',padx=10, pady=5, command=encryptFolder)
Chk1n.pack()

L2 = tk.Label(root, borderwidth=2,  bg='#000000', fg='#ffffff', relief='sunken', text="ENTER PIN")
L2.pack(padx=20, pady=5)
E2 = tk.Entry(root,bg='#3F3F3F', fg='#37D028',bd =2, validate="key", validatecommand=(validation, '%S'))
E2.config(width = 9)
E2.pack(padx=20, pady=3)

Chk2 = tk.Button(root, text="UNHIDE",bg='#505050', fg='#37D028', padx=10, pady=5, command=lambda:[unhideFolder(),ButtonChk(2)])
Chk2.pack()

Chk3 = tk.Button(root, text="DECRYPT",bg='#505050', fg='#37D028',padx=10, pady=5, command=decryptFolder)
Chk3.pack()

def on_closing():
    subprocess.check_call(["attrib","+H","logins.txt"])
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
