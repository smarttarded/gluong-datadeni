# import shutil
# shutil.move(src="C:/Users/khiem/github/gluong-datadeni/testtransfer.txt", dst="D:/testtransfer.txt")  
                        


# import os
# directory_path = os.getcwd()
# print("My current directory is : " + directory_path)
# folder_name = os.path.basename(directory_path)
# print("My directory name is : " + folder_name)


# def encripchun():
#     password = E1.get()
#     secFolder = folders.get()
#     dirArr = os.walk(f'{secFolder}')

#     for dirname, dirnames, filenames in dirArr:
#         for subdirname in dirnames:
#             print(os.path.join(dirname, subdirname))
#     for filename in filenames:
#         filePath = os.path.join(dirname, filename)
#         print(filePath)

#     fin = open(filePath, 'rt', encoding='utf-8')
#     file_contents = fin.read()
#     fout = open(filePath, 'wt', encoding='utf-8')

#     for char in str(file_contents):
#         charInt = ord(char) + int(password)
#         decrypted = chr(charInt)
#         fout.write(char.replace(char, decrypted))
#     if(f'{password}' == ''):
#         showinfo("DATADENI", "you must create a password.")
#         return None
#     else:
#         E1.delete(0, 'end')

# def decripchun():
#     password = E1.get()
#     secFolder = folders.get()
#     dirArr = os.walk(f'{secFolder}')

#     for dirname, dirnames, filenames in dirArr:
#         for subdirname in dirnames:
#             print(os.path.join(dirname, subdirname))
#     for filename in filenames:
#         filePath = os.path.join(dirname, filename)
#         print(filePath)

#     fin = open(filePath, 'rt', encoding='utf-8')
#     file_contents = fin.read()
#     fout = open(filePath, 'wt', encoding='utf-8')

#     for char in str(file_contents):
#         charInt = ord(char) - int(password)
#         decrypted = chr(charInt)
#         fout.write(char.replace(char, decrypted))
#     if(f'{password}' == ''):
#         showinfo("DATADENI", "you must create a password.")
#         password = 0
#         return None
#     else:
#         E1.delete(0, 'end')

# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# import os

# root = Tk()
# root.title("DATADENI")

# root.geometry("350x350")
# root.eval('tk::PlaceWindow . center')

# root.minsize(350, 320)
# root.maxsize(450, 450)
# dirArray2 = []
# folderPath = StringVar()
# folder_selected = filedialog.askdirectory()
# folderPath.set(folder_selected)
# directory_contents = os.listdir(folder_selected)
# for item in directory_contents:
#     if os.path.isdir(item):
#         print(item)
#         dirArray2.append(item)

# print(dirArray2)


# root.mainloop()

# count = 0
# d = "C:/Users/User1/github/gluong-datadeni/TestFart/"
# for path in os.listdir(d):
#     if os.path.isfile(os.path.join(d, path)):
#         count += 1
# print(count)

# from tkinter import ttk
# import tkinter as tk
# from tkinter.messagebox import showinfo
# # root window
# root = tk.Tk()
# root.geometry('300x120')
# root.title('Progressbar Demo')

# def update_progress_label():
#     return f"Current Progress: {pb['value']}%"

# def progress():
#     if pb['value'] < 100:
#         pb['value'] += 100 / 3
#         value_label['text'] = update_progress_label()
#     else:
#         showinfo(message='The progress completed!')
#         pb['value'] = 0

# def stop():
#     pb.stop()
#     value_label['text'] = update_progress_label()

# # progressbar
# pb = ttk.Progressbar(
#     root,
#     orient='vertical',
#     mode='determinate',
#     length=200
# )
# # place the progressbar
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# # label
# value_label = ttk.Label(root, text=update_progress_label())
# value_label.grid(column=0, row=1, columnspan=2)

# # start button
# start_button = ttk.Button(root,text='Progress', command=progress)

# start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

# root.mainloop()