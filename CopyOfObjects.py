import copy

l1=[56,78,100]

l2=l1

#l2=copy.copy(l1) 

#l2=l1.copy()

l2.append(200)
print(l2, id(l2))
print(l1, id(l1))

l1.pop(0)
print(l1)
print(l2)

if l1 is l2:
    print("L1 and L2 correspond to the same list")
else:
    print("L1 and L2 are two distinct list")
    


