import array as arr

a=arr.array('i',[1,2,3,4,5])
print(a)
a.append(7)
print(a)
a.insert(1,4)
print(a)
for p in a:
    print(p)
a.pop()
print(a)
a.remove(3)
print(a)
