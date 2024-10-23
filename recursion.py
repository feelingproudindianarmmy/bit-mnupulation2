def headrec(n,num):
    if n > num:
        return
    headrec(n+1,num)
    print(n)
n=int(input("enter the value n"))
headrec(1,n)