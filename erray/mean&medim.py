def array_mean(arr,array_size):
    total_sum=0
    for i in range(0,array_size):
        total_sum+=arr[i]

        return (total_sum/array_size)
def array_median(arr,array_size):
    sorted(arr)
    if array_size%!=0:
        return float(arr[int(array_size/2)])
    