
def isPrime(aNumber):
    if not isinstance(aNumber, int):
        raise Exception("Wrong argument given: should be an int!")
    
    if aNumber <= 1:
        raise ValueError("Wrong argument given: should be an int > 1!")
    
    for divisor in range(2,aNumber):
        if aNumber % divisor == 0:
            return False
        
    return True


try:
    print(isPrime(-3))
except:
    print("")
print('The end')
