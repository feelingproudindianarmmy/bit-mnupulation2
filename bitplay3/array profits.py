def calculateprofits(a,len):
    profits=0
    for i in range(1,len):
        if a[i]>a[i-1]:
            profits=profits+a[i]-a[i-1]
    return profits
a=[243,657,887,342,267,129]
len=len(a)
profit=calculateprofits(a,len)
print(profit)

