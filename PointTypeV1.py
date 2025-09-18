"""
The type Point should define 2 "attributes": x and y

The type Point should provide: 
    a constructor that do accept either 0 or 2 arguments
    a method clear
    a method distance
    a + operator
    

"""
import math

class Point: # __new__(), __init__(), __repr__(), __eq__()...
    def __init__(self, valx=0, valy=0):
        self.x=valx
        self.y=valy
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def clear(self):
        self.x=0
        self.y=0
    def distance(self, other):
        return math.sqrt((other.y-self.y)**2 + (other.x-self.x)**2)
    def __eq__(self, other):
        return self.x==other.x and self.y == other.y
    
p1=Point(2,3)

# p1=Point.__new__()
# p1.__init__(2,3)
# __init__(p1,2,3)

print(p1) # <2,3>
# print(p1.__repr__())

p2=Point()
# p1=Point.__new__()
# p1.__init__()
# __init__(p1)

print(p2) # <0,0>
p2.x=3
p2.y=9
print(p2) # <3,9>

print(p1.x) # 2
p1.x=5

print(p1) # <5,3>

p3=p1+p2

# p3=p1.__add__(p2)

print(p3) # <8,12>

p3.clear()
print(p3) # <0,0>

result=p1.distance(p2)
print(result) # a float value

print("p1",p1)
p2.x=5
p2.y=1
print("p2",p2)

if p1 == p2:
    print("P1 is equal to P2")
else:
    print("P1 is different from P2")





