#how to ask input from user
num=int(input("Enter an erray"))

#how to define any funtions like power set
def printpowerset(set,setsize):

#how to take some loops
for i in range(0,num):
    num2=int(input("enter element"))




#how to call the funtion
printpowerset(set,len(set))

#how to import any library(maths)
import math;

#nested loops

for i in range(0,num):
    for j in range(1,num):

#this things are very much neccasary or esantial  to understand and aply also..

#now practising all recursions programs

#number1

def headrec(n,num):
    if n > num:
        return
    headrec(n+1,num)
    print(n)
n=int(input("enter the value n"))
headrec(1,n)

#number2

def reversednumber(num):
    if(num > 0):
        last=num%10
        if (num//10>0):
            current_number=reversednumber(int(num//10))
            return last*pow(10,len(str(current_number)))+current_number
        return num
n=int(input("enter any number"))
print(reversednumber(n))

#number3

def reversedstring(s):
    if len(s)==1:
        return s[0]
    firstcharecter=s[0]
    return reversedstring(s[1:])+firstcharecter
b="adit jaldi"
print(reversedstring(b))
#practising the revers program

def reverse(arr,a_size,n):
    temp=0
    if(temp<a_size):
         start=temp
        end=min(temp+n-1,a_size-1)
          while(start<end):
          a[start],a[end]=a[end],a[start]
         start+=1
            end-=1
        temp+=n
a=[5,8,9,0,67]
a_size=len(a)
n=2
reverse(a,a_size,n)
for i in range(0,a_size):
 print (a[i],end=" ")