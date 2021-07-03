# import shutil
# shutil.move(src="C:/Users/khiem/github/gluong-datadeni/testtransfer.txt", dst="D:/testtransfer.txt")  
                        
def readLogins():
    s1 = open("hidepass.txt", "r").read()
    password = s1.split(' ')[0]
    folder = s1.split(' ')[1]
    loginSet = password + folder
    #print(password + folder)
    return loginSet

def ButtonChk(button_id):
    if button_id == 1:
        print(button_id)
        return 1
    if button_id == 2:
        print(button_id)
        return 2

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