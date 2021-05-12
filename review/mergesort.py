import copy

def mergesort(arr):
    if (len(arr) > 1):
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        
        # deep copy of list
        L_copy = copy.deepcopy(L)
        R_copy = copy.deepcopy(R)
        
        l = r = a = 0
        while (l < len(L_copy)) and (r < len(R_copy)):
            if L_copy[l] < R_copy[r]:
                arr[a] = L_copy[l]
                l += 1
            else:
                arr[a] = R_copy[r]
                r += 1
            a += 1
        while (l < len(L_copy)):
            arr[a] = L_copy[l]
            l += 1
            a += 1
        while (r < len(R_copy)):
            arr[a] = R_copy[r]
            r += 1
            a += 1
        
        
if __name__ == '__main__':
    arr = [-1,0,4,-4,4,8]
    print("Original arr ", arr)
    mergesort(arr)
    print(arr)
    
