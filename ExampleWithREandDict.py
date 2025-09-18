import re

def beginWith(aDict, aText):
    """

    Parameters
    ----------
    aDict : a dict
    aText : a string

    Returns
    -------
    newDict : a new dict that contains the element of aDict that have a 
    key that begin with the text aText (the test is case insensitive)

    """
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
    