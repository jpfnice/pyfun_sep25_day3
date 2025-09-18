import pickle
 
d=[
   {"name":"jean", 
   "city":"Geneva", 
   "Street name":"Grand pré", 
   "zip":23445, 
   "values":[1345, 67898, 789]
},
   {  "name":"Marc", 
      "city":"Nyon", 
      "Street name":"Grand pré", 
      "zip":23445, 
      "values":[13, 6898, 79]
   }
]

with open("output.txt", "bw") as myFile:
    pickle.dump(d, myFile)
    
    
print("The end")