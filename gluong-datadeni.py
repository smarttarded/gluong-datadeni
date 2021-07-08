from genericpath import exists
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import filedialog, ttk
import os
from tkinter.constants import X
import subprocess
from cryptography.fernet import Fernet
import shutil

#MADE BY [khiem g luong].
#smarttarded.github.io

root = tk.Tk()
root.title("DATADENI-GLUONG")

root.geometry("330x350")
root.eval('tk::PlaceWindow . center')

root.minsize(310, 350)
root.maxsize(400, 350)

root.iconbitmap('favicon.ico')

def getImgRoot():
    path = os.getcwd()
    return path

bg_img = tk.PhotoImage(file=f'{getImgRoot()}' + '\matrix.gif')
imglabel = tk.Label(root, image=bg_img)

os.system("attrib +h " + 'favicon.ico')
os.system("attrib +h " + 'matrix.gif')
os.system("attrib +h " + 'lib')
os.system("attrib +h " + 'python3.dll')
os.system("attrib +h " + 'python39.dll')
os.system("attrib +h " + 'hideimg.png')
os.system("attrib +h " + 'unhideimg.png')
os.system("attrib +h " + 'lockimg.png')
os.system("attrib +h " + 'unlockimg.png')
os.system("attrib +h " + 'hidepass.txt')


frameCnt = 27
frames = [PhotoImage(file=f'{getImgRoot()}' + '\matrix.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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

def hideFolder():
    if(ButtonChk(1)):
        secFolder = folders.get()
        password = E1.get()
        namer = open("hidepass.txt", "r")
        readfile = namer.read()
        if(f'{password}' == '') and f'{secFolder}' in readfile:
            showinfo("DATADENI-GLUONG", "Hiding folder with existing password")
            os.system("attrib +h " + f'{secFolder}')
            return password
        elif(f'{password}' == ''):
            showinfo("DATADENI-GLUONG", "you must create a password.")
            return 
        else:
            open("hidepass.txt", "a").write(password + ' ' + secFolder + '\n')
            subprocess.check_call(["attrib","+H","hidepass.txt"])
            os.system("attrib +h " + f'{secFolder}')
            E1.delete(0, 'end')

def unhideFolder():
    passCheck = readLogins()
    password = E1.get().strip()
    secFolder = folders.get().strip()
    passCheck2 = password + secFolder
    if(ButtonChk(2)):
        if(password == '666'):
            os.system("attrib -h " + f'{secFolder}')
            subprocess.check_call(["attrib","-H","hidepass.txt"])
        elif (passCheck.strip() == passCheck2.strip()):
            os.system("attrib -h " + f'{secFolder}')
            E1.delete(0, 'end')
        else:
            showinfo("DATADENI-GLUONG", "the password for this folder didn't match.")
            E1.delete(0, 'end')

def encryptFolder():
    secFolder = folders.get()
    driver = drivers.get().strip()
    arr = os.walk(f'{secFolder}')
    key_dst = os.path.realpath(driver)
    key_src = (os.getcwd() + ('\\' f'{secFolder}' + ".key"))
    if(ButtonChk(3)):
        if(secFolder == ''):
            showinfo("DATADENI-GLUONG", "you must select a folder for encryption.")
            return
        for dirname, dirnames, filenames in arr:
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
        if(driver == ''):
            showinfo("DATADENI-GLUONG", "you must select a key drive for encryption.")
            return 
        if(os.path.isfile(driver + '\\' + f'{secFolder}' + ".key")):
            showinfo("DATADENI-GLUONG", "reencrypting.")   
            decryptFolder()  
            dirFileCount()
            key = Fernet.generate_key()
            with open(f'{secFolder}' + ".key", 'ab') as mykey:
                mykey.write(key + b'\n')
            fernet = Fernet(key)
            for filename in filenames:
                f = open(os.path.join(dirname, filename), 'rb')
                original = f.read()
                source_path = os.path.join(dirname, filename)
                progress()
                encrypted = fernet.encrypt(original)
                with open(os.path.join(dirname, filename), 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
            shutil.move(src=key_src, dst=key_dst) 
            return
        for drive in driveArr:
            if(os.path.isfile(drive + (f'{secFolder}' + ".key"))):
                showinfo("DATADENI-GLUONG", "there is already an encryption key in one of the listed drives.")
                return
        else:
            with open(f'{secFolder}' + '.txt', 'w') as f:
                f.write('')
            shutil.move(src=os.getcwd() + ('\\'f'{secFolder}' + '.txt'), dst=getDirectory())

            dirFileCount()
            key = Fernet.generate_key()
            with open(f'{secFolder}' + ".key", 'ab') as mykey:
                mykey.write(key + b'\n')
            fernet = Fernet(key)
            for filename in filenames:
                f = open(os.path.join(dirname, filename), 'rb')
                original = f.read()
                progress()
                encrypted = fernet.encrypt(original)
                with open(os.path.join(dirname, filename), 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
            shutil.move(src=key_src, dst=key_dst) 
            encryptPin()
            return

def encryptPin():
    pin = E1.get().strip()
    secFolder = folders.get().strip()
    for num in str(pin):
        print(num)
    oldname = os.getcwd() + '\\' + f'{secFolder}' + ('\\'f'{secFolder}' + '.txt')
    newname = os.getcwd() + '\\' + f'{secFolder}' + ('\\'f'{pin}' + '.txt')
    print(oldname)
    os.rename(oldname, newname)
    return

def decryptFolder():
    secFolder = folders.get()
    driver = drivers.get().strip()
    arr = os.walk(f'{secFolder}')
    if(ButtonChk(4)):
        if(driver == ''):
            showinfo("DATADENI-GLUONG", "you must select a key drive for decryption.")
            return
        else:
            with open((driver + '\\' + (f'{secFolder}' + ".key")), 'rb') as mykey:
                key = mykey.read()
            fernet = Fernet(key)
            #drive_contents = os.listdir(driver)
            drive_keyloc = driver + '\\' + (f'{secFolder}' + ".key")
            if(os.path.isfile(drive_keyloc)):
                for dirname, dirnames, filenames in arr:
                    for subdirname in dirnames:
                        print(os.path.join(dirname, subdirname))
                    for filename in filenames:
                        f = open(os.path.join(dirname, filename), 'rb')
                        original = f.read()
                        source_path = os.path.join(dirname, filename)
                        #print("source path: " + source_path)                  
                        decrypted = fernet.decrypt(original)
                        with open(os.path.join(dirname, filename), 'wb') as decrypted_file:
                            decrypted_file.write(decrypted)
                os.remove(driver + '\\' + f'{secFolder}' + ".key")
            return

def ButtonChk(button_id):
    if button_id == 1:
        return 1
    if button_id == 2:
        return 2
    if button_id == 3:
        return 3
    if button_id == 4:
        return 4
        
def readLogins():
    s1 = open("hidepass.txt", "r").read()
    password = s1.split(' ')[0]
    folder = s1.split(' ')[1]
    loginSet = password + folder
    print(password + folder)
    return loginSet

def only_numbers(char):
    return char.isdigit()

def getDirectory():
    secFolder = folders.get()
    path = os.path.abspath(f'{secFolder}')
    print(path)
    return path
            
def dirFileCount():
    count = 0
    d = getDirectory()
    for path in os.listdir(d):
        if os.path.isfile(os.path.join(d, path)):
            count += 1
    return count

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

driveArr.append('::::')
if(os.path.exists('D:')):
    driveArr.append('D:')
    driveArr.remove('::::')
if(os.path.exists('E:')):
    #os.startfile("E:")
    driveArr.append('E:')
if(os.path.exists('F:')):
    driveArr.append('F:')
if(os.path.exists('G:')):
    driveArr.append('G:')

driveArrayList = list(driveArr)
drivers = StringVar(root)

OM0 = tk.OptionMenu(root, drivers,*driveArrayList)
OM0["menu"].config(bg='#3F3F3F', fg='#ffffff')
OM0.config(bg='#3F3F3F', fg='#ffffff')
OM0.place(relx=.8, rely = .02, width=55, height=36)

if(driveArr == ['::::']):
    OM0.destroy()
def setPin(text):
    E1.insert(END, text)

num1 = Button(root, fg="white", text ="1", bg = "#3F3F3F", command=lambda:setPin("1"))
num1.config(height = 2, width = 5)
num1.place(relx=.04, rely = .02)

num2 = Button(root, fg="white", text = "2", bg = "#3F3F3F", command=lambda:setPin("2"))
num2.config(height = 2, width = 5)
num2.place(relx=.04, rely = .22)

num3 = Button(root, fg="white", text ="3", bg = "#3F3F3F", command=lambda:setPin("3"))
num3.config(height = 2, width = 5)
num3.place(relx=.04, rely = .42)

num4 = Button(root, fg="white", text = "4", bg = "#3F3F3F", command=lambda:setPin("4"))
num4.config(height = 2, width = 5)
num4.place(relx=.04, rely = .62)

num5 = Button(root, fg="white", text ="5", bg = "#3F3F3F", command=lambda:setPin("5"))
num5.config(height = 2, width = 5)
num5.place(relx=.04, rely = .82)

num6 = Button(root, fg="white", text ="6", bg = "#3F3F3F", command=lambda:setPin("6"))
num6.config(height = 2, width = 5)
num6.place(relx=.22, rely = .02)

num7 = Button(root, fg="white", text = "7", bg = "#3F3F3F", command=lambda:setPin("7"))
num7.config(height = 2, width = 5)
num7.place(relx=.22, rely = .22)

num8 = Button(root, fg="white", text ="8", bg = "#3F3F3F", command=lambda:setPin("8"))
num8.config(height = 2, width = 5)
num8.place(relx=.22, rely = .42)

num9 = Button(root, fg="white", text = "9", bg = "#3F3F3F", command=lambda:setPin("9"))
num9.config(height = 2, width = 5)
num9.place(relx=.22, rely = .62)

num0 = Button(root, fg="white", text ="0", bg = "#3F3F3F", command=lambda:setPin("0"))
num0.config(height = 2, width = 5)
num0.place(relx=.22, rely = .82)

pb = ttk.Progressbar(
    root,
    style="red.Horizontal.TProgressbar",
    orient='vertical',
    mode='determinate',
    length=180,
)
s = ttk.Style()
s.theme_use('alt')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
pb.place(relx=.85, rely = .42)

def update_progress_label():
    return f"Current Progress: {pb['value']}%"

def progress():
    if pb['value'] < 100:
        pb['value'] += 100 / dirFileCount()
        # value_label['text'] = update_progress_label()
    if pb['value'] > 99.9:
        showinfo("DATADENI-GLUONG", 'encrypted ' + f'{dirFileCount()}' + ' files')
        pb['value'] = 0

hideimg = tk.PhotoImage(file =f'{getImgRoot()}' + '\\' + 'hideimg.png')
hidess = hideimg.subsample(6,6)
Chk1 = tk.Button(root, image = hidess ,bg='#3F3F3F', fg='#37D028',padx=10, pady=5, borderwidth=3, relief="ridge", command=lambda:[hideFolder(),ButtonChk(1)])
Chk1.config(height = 32, width = 32)
Chk1.place(relx=.65, rely = .62)

unhideimg = tk.PhotoImage(file =f'{getImgRoot()}' + '\\' + "unhideimg.png")
unhidess = unhideimg.subsample(6,6)
Chk2 = tk.Button(root, image = unhidess,bg='#3F3F3F', fg='#37D028', padx=10, pady=5, borderwidth=3, relief="ridge",command=lambda:[unhideFolder(),ButtonChk(2)])
Chk2.config(height = 32, width = 32)
Chk2.place(relx=.65, rely = .82)

lockimg = tk.PhotoImage(file =f'{getImgRoot()}' + '\\' + "lockimg.png")
lockss = lockimg.subsample(6,6)
Chk1n = tk.Button(root, image=lockss,bg='#3F3F3F', fg='#37D028',padx=10, pady=5, borderwidth=3, relief="ridge",command=lambda:[encryptFolder(),ButtonChk(3)])
Chk1n.config(height = 32, width = 32)
Chk1n.place(relx=.4, rely = .62)

unlockimg = tk.PhotoImage(file =f'{getImgRoot()}' + '\\' + "unlockimg.png")
unlockss = unlockimg.subsample(6,6)
Chk3 = tk.Button(root, image=unlockss,bg='#3F3F3F', fg='#37D028',padx=10, pady=5, borderwidth=3, relief="ridge", command=lambda:[decryptFolder(),ButtonChk(4)])
Chk3.config(height = 32, width = 32)
Chk3.place(relx=.4, rely = .82)

def getFolderPath():
    dirArray = []
    if not dirArray:
        dirArray.clear()
    folder_selected = filedialog.askdirectory()
    folders.set(folder_selected)
    sourcePath = folders.get()
    os.chdir(sourcePath)
    directory_contents = os.listdir(folder_selected)
    for item in directory_contents:
        if os.path.isdir(item):
            dirArray.append(item)
    for f in directory_contents:
        if f.startswith('__' or 'lib'):
            dirArray.remove(f)
    return dirArray

folders = StringVar(root)
dirArrayList = getFolderPath()
OM1 = tk.OptionMenu(root, folders, *dirArrayList)
OM1["menu"].config(bg='#3F3F3F', fg='#ffffff')
OM1.config(bg='#3F3F3F', fg='#ffffff')
OM1.place(relx=.4, rely = .02, relwidth=0.36, height= 36)
folders.set('') 

E1 = tk.Entry(root,bg='#3F3F3F', fg='#37D028',bd =2, validate="key", textvariable=var, validatecommand=(validation, '%S'))
E1.place(relx=.4, rely = .41, relwidth=0.36)

def on_closing():
    subprocess.check_call(["attrib","+H","hidepass.txt"])
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
