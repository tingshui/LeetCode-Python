def quicksort(arr, start, end):
    if (start < end):
        p = partition(arr, start, end)
        quicksort(arr, start, p-1)
        quicksort(arr, p+1, end)

def partition(arr, start, end):
    i = start - 1
    piviot_v = arr[end]
    for j in range(start, end):
        if arr[j] <= piviot_v:
            i += 1
            swap(arr, j, i)           
    swap(arr, i+1, end)
    return (i+1)
            
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
                
        
if __name__ == '__main__':
    arr = [-1,0,4,-4,4,8]
    print("Original arr ", arr)
    quicksort(arr, 0, len(arr)-1)
    print(arr)
