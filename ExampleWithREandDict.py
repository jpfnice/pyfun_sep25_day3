import re

def beginWith(aDict, aText):
    newDict={}
    for k in aDict.keys():
        if re.match(f"^{aText}.*", k, re.IGNORECASE):
            newDict[k]=aDict[k]
    return newDict


d1={
    "maria":27845676, 
    "peter":27867899,
    "pierre":3446788,
    "marco":6787778,
    "adele":7898889,
    "muriel":8988766
}          

result=beginWith(d1,"MA")
print(len(result), "elements match your pattern:")
print(result)
    