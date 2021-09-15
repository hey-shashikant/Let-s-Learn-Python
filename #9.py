num = 5
#to access the address
print(id(num))
s = 'shashikant'
print(id(s))

a = 10
b = a
c = 10
"""
In python if multiple varibales have same data
they will have same address
"""
if(id(a) == id(b) and id(b) == id(c)):
	print("address are same")
else:
	print("address are different")
"""
whenever a value is not tagged by a variable 
later they will be collected by garbage collector.
"""
#constants
"""
in python we don't have constants we can modify them
"""

#type of variable
print(type(a))


