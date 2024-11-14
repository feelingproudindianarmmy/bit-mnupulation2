def haoi(n,a,b,c):
    if n==1:
        print("move disk" ,n, "from rod",a,"to rod",b)
        return
    haoi(n-1,a,c,b)
    print("move disk" ,n, "from rod",a,"to rod",b)
    haoi(n-1,c,b,a)
n=4
haoi(n,'A','C','B')
