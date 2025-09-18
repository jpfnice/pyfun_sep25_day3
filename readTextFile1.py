

# myFile=open("data.txt")

# for e in myFile:
#     print(e)
    
# myFile.close()

import os.path

fname="data56756.txt"

if os.path.exists(fname):
    with open("data.txt") as myFile:
        for e in myFile:
            e=e.rstrip()
            print(e)
else:
    print(fname, "does not exists")      
        
print("The end")