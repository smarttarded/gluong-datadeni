import os
  
# take Input from the user 
#query = input("Which drive you have to open ? C , D or E: \n")
  
# Check the condition for 
# opening the C drive
def keyPasser():
    if(os.path.exists('D:')):
        os.startfile("D:")
    if(os.path.exists('E:')):
        os.startfile("E:")
    else:
        return None

def encripchun():
    password = E1.get()
    secFolder = folders.get()
    dirArr = os.walk(f'{secFolder}')

    for dirname, dirnames, filenames in dirArr:
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
    for filename in filenames:
        filePath = os.path.join(dirname, filename)
        print(filePath)

    fin = open(filePath, 'rt', encoding='utf-8')
    file_contents = fin.read()
    fout = open(filePath, 'wt', encoding='utf-8')

    for char in str(file_contents):
        charInt = ord(char) + int(password)
        decrypted = chr(charInt)
        fout.write(char.replace(char, decrypted))
    if(f'{password}' == ''):
        showinfo("DATADENI", "you must create a password.")
        return None
    else:
        E1.delete(0, 'end')

def decripchun():
    password = E1.get()
    secFolder = folders.get()
    dirArr = os.walk(f'{secFolder}')

    for dirname, dirnames, filenames in dirArr:
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
    for filename in filenames:
        filePath = os.path.join(dirname, filename)
        print(filePath)

    fin = open(filePath, 'rt', encoding='utf-8')
    file_contents = fin.read()
    fout = open(filePath, 'wt', encoding='utf-8')

    for char in str(file_contents):
        charInt = ord(char) - int(password)
        decrypted = chr(charInt)
        fout.write(char.replace(char, decrypted))
    if(f'{password}' == ''):
        showinfo("DATADENI", "you must create a password.")
        password = 0
        return None
    else:
        E1.delete(0, 'end')

def readLogins():
    s1 = open("hidepass.txt", "r").read()
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