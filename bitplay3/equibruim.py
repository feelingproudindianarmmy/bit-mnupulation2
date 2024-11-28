def equibruimpoint(arr):
    leftsidesum=0
    rightsidesum=0
    n=len(arr)

    for i in range(n):
        leftsidesum=0
        rightsidesum=0
        for j in range(i):
            leftsidesum+=arr[j]
        for j in range(i+1,n):
            rightsidesum+=arr[j]
        if leftsidesum==rightsidesum:
            return i
    
a=[1,2,3,2,1]
print(equibruimpoint(a))