def partition(arr, start, end):
    i = start -1
    pivot_v = arr[end]
    for j in range(start, end):
        if (arr[j] < pivot_v):
            i += 1
            swap(arr, i, j)
    swap(arr, end, i+1)
    return (i+1)        


def quickselect(arr, k, start, end):
    pivot_index = partition(arr, start, end)
    # notice r_pivot_index
    r_pivot_index = pivot_index - start + 1
    if (r_pivot_index == k):
        return arr[pivot_index]
    elif (r_pivot_index < k):
        return quickselect(arr, k-r_pivot_index, pivot_index+1, end)
    else:
        return quickselect(arr, k, start, pivot_index-1)
    
            
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
                
        
if __name__ == '__main__':
    arr = [-1,0,4,-4,4,8]
    print("Original arr ", arr)
    r = quickselect(arr, 4, 0, len(arr) -1)
    print(r)
    