# 'r' 'w' 'a' 'r+' 'w+' 'a+' 
nb=3
with open("output.txt", "w") as myFile:
    print("Current position:",myFile.tell())
    # myFile.write("Line 1\n")
    # myFile.write("Line 2")
    # myFile.write("Line 3")
    print("line 1", nb, "nb**2", nb**2, file=myFile, sep=":", end="")
    print("line 2", file=myFile)
    print("line 3", file=myFile)
    # print("Current position:",myFile.tell())
    
print("The end")