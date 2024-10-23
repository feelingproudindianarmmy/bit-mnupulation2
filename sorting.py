
def checksorted(a):

    length=len(a)
    if length==0 or length==1:
        return True
    return a[0]<=a[1] and checksorted(a[1:])
a={1,2,3,4,5,6,7}
if checksorted(a):
    print("it is an sorted erray")
else:
    print("its not sorted")