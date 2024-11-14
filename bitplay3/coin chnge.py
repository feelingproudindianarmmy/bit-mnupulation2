#number1
def count(S, m, n):
    
    table = [[0 for x in range(m)] for x in range(n+1)]
 
    
    for i in range(m):
        table[0][i] = 1
    
    for i in range(1,n+1):
        for j in range(m):

            x=table[i-S[j]][j] if i-S[j]>=0 else 0

        y = table[i][j-1] if j >= 1 else 0
        table[i][j] = x + y
        return table[n][m-1]
arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))

#number2
def count_ways(coins, total): #1 first we will simply define the ways of count as (coins and total)
    
    ways = [0] * (total + 1)  #4 then the we will write ways as 0 multiplied by the total(5)+1

    ways[0] = 1 #5 the it will be ways 0 as 1

    
    for coin in coins:#6 then we  will take loop that for coin in coin
        
        for amount in range(coin, total + 1):#7again we will put loop in loop

            ways[amount] += ways[amount - coin]#8 then we will take ways amount plus ways amount - the coin ,that is [1,2,5]

    return ways[total] #9 it will now return the ways as the total


coins = [1, 2, 5]#2then we will take [1,2,5] in coins

total = 5          #3 we will take 5 as total

result = count_ways(coins, total)#10 now,finally result will be that (count ways)=(coins,total)

print("Number of ways to make change")#11 at last it will print ("Number of ways to make change")

#12 we learn and made the project which tells us counting ways of coins and its total too.
#13we used loops and nested loops and made list in this project too.


 