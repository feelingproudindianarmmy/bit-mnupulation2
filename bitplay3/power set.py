import math;
def printpowerset(set,setsize):
set=[]

Er=int(input("enter you erray size"))
for i in range(0,Er):
    Er1=int(input("enter yor element"))
    set.append(Er1)
printpowerset(set,len(set))