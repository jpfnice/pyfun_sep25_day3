


with open("mydata.txt") as myFile:
    print("Current position:",myFile.tell())
    text=myFile.read(5)
    print(text)
    text=myFile.read(5)
    print(text)
    print("Current position:",myFile.tell())
    # text=myFile.read(5)
    # print(text)
    # print("Current position:",myFile.tell())
    myFile.seek(0)
    print("Current position:",myFile.tell())
    print("After seek(0)")
    text=myFile.read(5)
    print(text)
    print("Current position:",myFile.tell())
print("The end")