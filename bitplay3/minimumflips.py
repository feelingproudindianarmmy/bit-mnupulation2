def minFlips(arr):
    
    count_zeros = arr.count(0)
    count_ones = len(arr) - count_zeros  
    
    flips_to_all_ones = count_zeros

    
    flips_to_all_zeros = count_ones

    
    return min(flips_to_all_ones, flips_to_all_zeros)


arr = [0, 1, 0, 1, 1, 0]
print(minFlips(arr))  