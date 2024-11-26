def push_zeroes_to_end(arr):
   
    write = 0
    
    
    for read in range(len(arr)):
        
        if arr[read] != 0:
           
            if read != write:
                arr[write] = arr[read]
                arr[read] = 0  
            write += 1
    
    return arr


arr = [0, 1, 0, 3, 12]
print("Original Array:", arr)
result = push_zeroes_to_end(arr)
print("Array after pushing zeroes to the end:", result)

