def maxsubarraysum(a,a_size):
    max=a[0]
    cmax=0

    for i in range(0,a_size):
        cmax=cmax+a[i]

        if(max<cmax):
            max=cmax
        if cmax<0:
            cmax=0
    return max
a=[1,-3,6,7,-9,-2,5,-7,4,-9]
len=len(a)
print(maxsubarraysum(a,len))
    