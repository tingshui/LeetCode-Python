# n is used to control the heap size
def heapify(arr, i, n):
    l = 2*i+1
    r = 2*i+2
    largest = i
    if (l<n) and (arr[l] >arr[i]):
        largest = l
    if (r<n) and (arr[r]>arr[largest]):
        largest = r
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest, n)

def heapsort(arr):
    # bottom up, convert array to max-heap
    # max-heap, not sorting, only parent>child
    # Array[n/2+1, ...n] are all leaves of the trees
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)
    
    for i in range(n-1, 0, -1):
        swap(arr, i, 0)
        heapify(arr, 0, i)
            
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
                
        
if __name__ == '__main__':
    arr = [-1,0,4,-4,4,8]
    print("Original arr ", arr)
    heapsort(arr)
    print(arr)
