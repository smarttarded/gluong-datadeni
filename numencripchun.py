import os
import io
from typing_extensions import TypeVarTuple

def getfiles(selection):
    dir = os.listdir(selection)
    dirArr = os.walk(selection)
    for dirname, dirnames, filenames in dirArr:
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
    for filename in filenames:
        filePath = os.path.join(dirname, filename)
        print(filePath)
        f = open(filePath.split(), 'r')
        file_contents = f.read()
        print (file_contents)

    # for file in dir:
    #     print(file)


# c='p'
# x=ord(c)
# #it will give you the ASCII value stored in x
# print(x)'

fin = open('TestFolder/testtext.txt', 'rt', encoding='utf-8')
file_contents = fin.read()

fout = open('TestFolder/testtext.txt', 'wt', encoding='utf-8')

# teststr = 'amogus is sus?'
# otherInt = 6
# for char in str(file_contents):
#     charInt = ord(char) + otherInt
#     decrypted = chr(charInt)
#     fout.write(char.replace(char, decrypted))

otherInt = 6
for char in str(file_contents):
    charInt = ord(char) - otherInt
    decrypted = chr(charInt)
    fout.write(char.replace(char, decrypted))



import usb.core

devices = usb.core.find(find_all=True)

dev = next(devices)

print("device bus:", dev.bus)
print("device address:", dev.address)
print("device port:", dev.port_number)
print("device speed:", dev.speed)
