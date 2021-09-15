l1 = [1,2,3,4,5,6]
print(l1)

l2 = [1,'a',"shashikant",2,3,4]
print(l2)

print(l2[2])

print(l2[-1])

print(l2[1:])

names = ['shashikant','gunjan','garv']
print(names)

print(names[1])

m1 = [l2,names]
print(m1)

l2.append(10)
print(l2)

l1.clear()
print(l1)

l2.remove('a')

print(l2)

l2.pop(1)

print(l2)

#List by default follows stack
l2.pop()
print(l2)

l2.extend([1,2,3,4,5])
print(l2)

print(min(l2))
print(max(l2))
print(sum(l2))
l2.sort()
print(l2)