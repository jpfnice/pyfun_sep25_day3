"""
The = operator (assigment operator) does not create a copy of the value you assign .
If you want to create a copy, you can use the function copy() of the copy module, or a copy() method if one exists

"""

import copy

l1=[56,78,100]

#l2=l1
#l2=l1.copy() # The copy method of list is used
l2=copy.copy(l1) # The copy() function of the module copy is used

print("l1", l1)
print("l2", l2)

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
    


