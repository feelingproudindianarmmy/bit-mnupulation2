def power2(number):
        if(number==0):
            return 0
        if((number&(~(number-1)))==number):
            return 1
        return 0
number=int(input("enter any number"))
if(power2(number)):
    print("power of 2")
else:
    print("not a power of 2")

