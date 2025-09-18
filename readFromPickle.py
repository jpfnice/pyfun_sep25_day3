import pickle
 

with open("output.txt", "br") as myFile:
    d=pickle.load(myFile)
    
print(d)    

print("The end")