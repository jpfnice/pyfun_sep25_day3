

d=[12,34,56]

first,second,third=d # unpacking assignment

print(first, "<=>", d[0])
print(second, "<=>", d[1])
print(third, "<=>", d[-1])

# first,second=d # Error! : not enough variable given, toomany value to unpack

d=[12,34,56,78,89,12,89,100]

first,*other,last=d

print(first, "<=>", d[0])
print(other)
print(last, "<=>", d[-1])