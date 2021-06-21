# 1. 冒泡排序
# 时间复杂度：O(n2), 稳定性：稳定
# 描述：从头到尾比较相邻两个元素，如果第一个比第二个大，则交换位置
# 特点：比较适合小数据的排序。但是，由于算法复杂度较高，在数据量大的时候不适合使用。

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
#代码优化：增加一个swap标志，若一次循环中没有任何值交换位置，则说明排序已经完成，跳出即可。 
def bubbleSort2(array):
    for i in range(len(array)):
        swap = False
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swap = True
        if not swap:
            break

# 2. 选择排序
# 时间复杂度：O(n2), 稳定性：不稳定 
# 描述：在未排序的序列中找出最小的元素，存放到数组的开始位置；
def selectSort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        
# 3. 插入排序
# 时间复杂度：O(n2), 稳定性：不稳定 
# 描述： 将序列分为已排序和未排序两段，每次将未排序的第一个元素插入前面已排序的正确位置；
def insertionSort(array):
    for i in range(len(array)-1):
        cur = array[i+1]
        pos = i
        while cur < array[pos] and pos >= 0:
            array[pos +1] = array[pos]
            pos -= 1
        array[pos + 1] = cur
        
# 4. 希尔排序
# 希尔排序虽然快，但是毕竟是插入排序，其数量级并没有后起之秀——快速排序快。在大量数据面前，希尔排序不是一个好的算法。但是，中小型规模的数据完全可以使用它。
# 5. 归并排序
# 归并排序在数据量比较大的时候也有较为出色的表现，但是，其空间复杂度使得在数据量特别大的时候几乎不可接受。考虑到有的机器内存本身就比较小，因此，采用归并排序一定要注意。
# 6. 快速排序
# 快速排序是原地排序，不占用额外空间。快速排序尤其在数据量大的时候性能优越性更加明显。但是在必要的时候，需要考虑优化以提高其在最坏情况下的性能。
# 7. 堆排序
# 堆排序在建立堆和调整堆的过程中会产生比较大的开销，在元素少的时候并不适用。但是，在元素比较多的情况下，还是不错的一个选择。尤其是在解决诸如“前n大的数”一类问题时，几乎是首选算法。

def test():
    a = [2,5,1,3, -1, 0]
    b = mergesort(a)
    print(b)
            

if __name__ == '__main__':
    test()



