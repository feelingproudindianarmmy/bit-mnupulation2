def maxones(a,a_size):
    counter=0
    maxones=0
    for i in range(0,a_size):
      if a[i]==0:
        counter=0
      else:
         
         counter+=1
         maxones=max(counter,maxones)
    return maxones
a=[0,1,1,0,1,0,1,0,0,1]
len=len(a)
print(maxones(a,len))
    