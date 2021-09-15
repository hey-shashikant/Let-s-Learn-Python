#Data types in python

# 1. None
"""
if a variable is not assigned with any value
"""

#2. Numeric

"""
int, float , complex, bool
"""
x = 5;
print(type(x))
x = 10.5
print(type(x))

num = 5+10j
print(type(num))

a = 5.6
b = int(a)
print(b)

k = float(b)
print(k)

c = complex(b,k)
print(c)

#3. Bool
t = b < k
print(t)

print(int(True))
print(int(False))

#4 . Lists

l1 = [1,2,3,4,5]
print(l1)

print(type(l1))

#5. set

t = {1,2,3,4,5}
print(type(t))

#6. Tuple
p = (1,2,3,4,5)
print(type(p))

# strings
"""
python does not support character instead it treats it as string only
"""
s = 'a'
print(type(s))

# range
l1 = list(range(0,10))
print(l1)

# Dictionary

"""
Dictionary is like hashing in cpp where we map each value with a key
Key must be unique
"""

di = {'preeti':24,'sudhir':28,'jyoti':30}
print(di['preeti'])
print(di['sudhir'])
print(di.get('jyoti'))

