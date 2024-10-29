def ways(stairs):
    if stairs<0:
        return 0
    if stairs==0:
        return 1
    twostep=0
    onestep=0

    if (stairs>=2):
        twostep=ways(stairs-2)
    onestep=ways(stairs-1)

    return twostep+onestep
n=int(input("enter your steps of stairs"))
print(ways(n))
