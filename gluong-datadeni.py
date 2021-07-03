import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
import os
from tkinter.constants import X
import subprocess
from cryptography.fernet import Fernet
from numencripchun import *
import shutil

#MADE BY [khiem g luong].

root = tk.Tk()
root.title("DATADENI")

root.geometry("350x350")
root.eval('tk::PlaceWindow . center')

root.minsize(350, 320)
root.maxsize(450, 480)

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
imglabel.place(height=800, width=475,y=-220)
root.after(0, update, 0)

path = '.'
dirArray = []

directory_contents = os.listdir(path)
for item in directory_contents:
    if os.path.isdir(item):
        print(item)
        dirArray.append(item)

for f in directory_contents:
    if f.startswith('lib' or '.git'):
        dirArray.remove(f)


def hideFolder():
    secFolder = folders.get()
    password = E1.get()
    arr = os.walk(f'{secFolder}')
    if(ButtonChk(1)):
        for dirname, dirnames, filenames in arr:
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
        for filename in filenames:
            print(os.path.join(dirname, filename))
        
        if(f'{password}' == ''):
            showinfo("DATADENI", "you must create a password.")
            return None
        else:
            open(f'{secFolder}'+".hide", "a").write(password + ' ' + secFolder)
            for files in os.listdir(f'{secFolder}'):
                print("checkFolder " + files)
                os.system("attrib +h " + files)
            os.system("attrib +h " + f'{secFolder}')
            subprocess.check_call(["attrib","+H","f'{secFolder}'.hide"])
            E1.delete(0, 'end')

def unhideFolder():
    passCheck = readLogins()
    password2 = E1.get()
    secFolder = folders.get()
    passCheck2 = password2 + secFolder
    if(ButtonChk(2)):
        if(password2 == 'pluriselect'):
            os.system("attrib -h " + f'{secFolder}')
            subprocess.check_call(["attrib","-H","hidepass.txt"])
        elif (passCheck.strip() == passCheck2.strip()):
            os.system("attrib -h " + f'{secFolder}')
        else:
            showinfo("DATADENI", "the password for this folder didn't match.")
        E1.delete(0, 'end')

def encryptFolder():
    secFolder = folders.get()
    driver = drivers.get().strip()
    arr = os.walk(f'{secFolder}')
    key_dst = os.path.realpath(driver)
    #print("keydst " + key_dst + (f'{secFolder}' + ".key"))
    for dirname, dirnames, filenames in arr:
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
    for drive in driveArr:
        print(drive)
        if(os.path.isfile(drive+ (f'{secFolder}' + ".key"))):
            showinfo("DATADENI", "there is already an encryption kee in one of the listed drives.")
            return None
    if(driver == "KEE"):
        showinfo("DATADENI", "you must select a kee drive for encryption.")
        return None
    else:
        key = Fernet.generate_key()
        with open(f'{secFolder}' + ".key", 'ab') as mykey:
            mykey.write(key + b'\n')
        fernet = Fernet(key)
        for filename in filenames:
            f = open(os.path.join(dirname, filename), 'rb')
            original = f.read()
            source_path = os.path.join(dirname, filename)
            print("source path: " + source_path)
            encrypted = fernet.encrypt(original)
            with open(os.path.join(dirname, filename), 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            key_src = (os.getcwd() + ('\\' f'{secFolder}' + ".key"))
        shutil.move(src=key_src, dst=key_dst) 

def decryptFolder():
    secFolder = folders.get()
    driver = drivers.get().strip()
    arrFolder = os.walk(f'{secFolder}')
    if(driver == "KEE"):
        showinfo("DATADENI", "you must select a key drive for decryption.")
    else:
        drive_contents = os.listdir(driver)
        drive_keyloc = driver + '\\' + (f'{secFolder}' + ".key")
        if(os.path.isfile(drive_keyloc)):
            print(drive_keyloc)
        else:
            print("key not found in drive")
            print(drive_contents)
        #if(driver)
        # for dirname, dirnames, filenames in arrFolder:
        #     for subdirname in dirnames:
        #         os.path.join(dirname, subdirname)
        # for filename in filenames:
        #     if(os.path.exists(f'{secFolder}'+'.key')):
        #         with open(f'{secFolder}' + ".key", 'rb') as mykey:
        #             key = mykey.read()
        #         fernet = Fernet(key)
        #         f = open(os.path.join(dirname, filename), 'rb')
        #         original = f.read()
        #         decrypted = fernet.decrypt(original)
        #         with open(os.path.join(dirname, filename), 'wb') as decrypted_file:
        #             decrypted_file.write(decrypted)
        #     else:
        #         showinfo("DATADENI", "there is already a encryption key for this folder.")

def only_numbers(char):
    return char.isdigit()

def on_write(*args):
    s = var.get()
    if len(s) > 0:
        if not s[-1].isdigit(): 
            var.set(s[:-1])
        else: 
            var.set(s[:max_len])
max_len = 5
var = StringVar()
var.trace("w", on_write) 
validation = root.register(only_numbers)

driveArr = []
def keyPasser():
    if(os.path.exists('D:')):
        driveArr.append('D:')
    if(os.path.exists('E:')):
        #os.startfile("E:")
        driveArr.append('E:')
    if(os.path.exists('F:')):
        driveArr.append('F:')
    else:
        return 
keyPasser()

driveArrayList = list(driveArr)
drivers = StringVar(root)
drivers.set('KEE')
OM0 = tk.OptionMenu(root, drivers,*driveArrayList)
OM0["menu"].config(bg='#000000', fg='#ffffff')
OM0.place(relx=.82, rely = .02, width=60)

def setPin(text):
    E1.insert(END, text)

# scroll_bar = Scrollbar(root)
# scroll_bar.pack( side = RIGHT,
#                 fill = Y )  
# mylist = Listbox(root, 
#                  yscrollcommand = scroll_bar.set ) 
# for line in range(1, 26):
#     mylist.insert(END, "Geeks " + str(line))
# mylist.pack( side = LEFT, fill = BOTH )
#scroll_bar.config( command = mylist.yview )

num1 = Button(root, text ="1", bg = "gray", command=lambda:setPin("1"))
num1.config(height = 2, width = 5)
num1.place(relx=.05, rely = .02)

num2 = Button(root, text = "2", bg = "gray", command=lambda:setPin("2"))
num2.config(height = 2, width = 5)
num2.place(relx=.05, rely = .22)

num3 = Button(root, text ="3", bg = "gray", command=lambda:setPin("3"))
num3.config(height = 2, width = 5)
num3.place(relx=.05, rely = .42)

num4 = Button(root, text = "4", bg = "gray", command=lambda:setPin("4"))
num4.config(height = 2, width = 5)
num4.place(relx=.05, rely = .62)

num5 = Button(root, text ="5", bg = "gray", command=lambda:setPin("5"))
num5.config(height = 2, width = 5)
num5.place(relx=.05, rely = .82)

num6 = Button(root, text ="6", bg = "gray", command=lambda:setPin("6"))
num6.config(height = 2, width = 5)
num6.place(relx=.23, rely = .02)

num7 = Button(root, text = "7", bg = "gray", command=lambda:setPin("7"))
num7.config(height = 2, width = 5)
num7.place(relx=.23, rely = .22)

num8 = Button(root, text ="8", bg = "gray", command=lambda:setPin("8"))
num8.config(height = 2, width = 5)
num8.place(relx=.23, rely = .42)

num9 = Button(root, text = "9", bg = "gray", command=lambda:setPin("9"))
num9.config(height = 2, width = 5)
num9.place(relx=.23, rely = .62)

num0 = Button(root, text ="0", bg = "gray", command=lambda:setPin("0"))
num0.config(height = 2, width = 5)
num0.place(relx=.23, rely = .82)

folders = StringVar(root)
folders.set(dirArray[0]) 
dirArrayList = list(dirArray)
OM1 = tk.OptionMenu(root, folders, *dirArrayList)
OM1["menu"].config(bg='#000000', fg='#ffffff')
OM1.place(relx=.41, rely = .02, relwidth=0.38)

# L1 = tk.Label(root, borderwidth=2, bg='#000000', fg='#ffffff', relief='sunken', text="CREATE PIN")
# L1.place(relx=.4, rely = .13)
# E1 = tk.Entry(root, bg='#3F3F3F', fg='#37D028', bd =2, validate="key", validatecommand=(validation, '%S'))
# E1.bind("<BackSpace>", delete_entry)
# E1.config(width = 9)
# E1.place(relx=.4, rely = .23)

# L2 = tk.Label(root, borderwidth=2,  bg='#000000', fg='#ffffff', relief='sunken', text="ENTER PIN")
# L2.place(relx=.4, rely = .13)
E1 = tk.Entry(root,bg='#3F3F3F', fg='#37D028',bd =2, validate="key", textvariable=var, validatecommand=(validation, '%S'))
E1.place(relx=.41, rely = .41, relwidth=0.38)

hideimg = tk.PhotoImage(file ="hideimg.png")
hidess = hideimg.subsample(6,6)
Chk1 = tk.Button(root, image = hidess ,bg='#505050', fg='#37D028',padx=10, pady=5, command=lambda:[hideFolder(),ButtonChk(1)])
Chk1.config(height = 40, width = 40)
Chk1.place(relx=.71, rely = .63)

unhideimg = tk.PhotoImage(file ="unhideimg.png")
unhidess = unhideimg.subsample(6,6)
Chk2 = tk.Button(root, image = unhidess,bg='#505050', fg='#37D028', padx=10, pady=5, command=lambda:[unhideFolder(),ButtonChk(2)])
Chk2.config(height = 40, width = 40)
Chk2.place(relx=.71, rely = .83)

Chk1n = tk.Button(root, text="ENCRYPT",bg='#505050', fg='#37D028',padx=10, pady=5, command=encryptFolder)
Chk1n.place(relx=.41, rely = .64)


Chk3 = tk.Button(root, text="DECRYPT",bg='#505050', fg='#37D028',padx=10, pady=5, command=decryptFolder)
Chk3.place(relx=.41, rely = .84)

def on_closing():
    subprocess.check_call(["attrib","+H","hidepass.txt"])
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
