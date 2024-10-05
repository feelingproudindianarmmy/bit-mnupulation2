#swapping by method no.1
def swap1(a,b):
    a=a^b
    b=a^b
    a=a^b
    print(a,b)
swap1(1,2)
#swapping by method no.2
def swap2(a,b):
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print(a,b)
swap2(4,7)