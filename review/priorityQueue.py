import heapq
from queue import PriorityQueue

# heapq
# -基于list的二叉堆；-能在时间内插入和获取最小的元素 O(log n)。
# -由于heapq在技术上只提供最小堆实现，因此必须添加额外步骤来确保排序稳定性，以此来获得“实际”的优先级队列中所含有的预期特性。
def pq1():
    pq = []
    heapq.heappush(pq, (2, 'second'))
    heapq.heappush(pq, (1, 'first'))
    heapq.heappush(pq, (3, 'third'))

    while pq:
        next = heapq.heappop(pq)
        print(next)

class cust_pq():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, other):
        if self.key == other.key:
            return self.value < other.value
        else:
            return self.key < other.key
    #   def __str__(self):
    #       return str(self.key) + " " + str(self.value)
    def __repr__(self):
        return "(" + str(self.key) + " , " + str(self.value) + ")"

def cust_pq1():
    heap = []
    heapq.heappush(heap, cust_pq(1, 5))
    heapq.heappush(heap, cust_pq(1, 3))
    heapq.heappush(heap, cust_pq(2, 2))
    heapq.heappush(heap, cust_pq(2, 7))
    heapq.heappush(heap, cust_pq(2, 3))
    heapq.heappush(heap, cust_pq(4, 3))
    heapq.heappush(heap, cust_pq(10, 1))
    while heap:
        print(heapq.heappop(heap))


# queue.PriorityQueue这个优先级队列的实现在内部使用了heapq，时间和空间复杂度与heapq相同。
# 区别在于PriorityQueue是同步的，提供了锁语义来支持多个并发的生产者和消费者。锁语义可能会带来帮助，也可能会导致不必要的开销。
def pq2():
    pq = PriorityQueue()
    pq.put((2, 'second'))
    pq.put((1, 'first'))
    pq.put((3, 'third'))

    while not pq.empty():
        next = pq.get()
        print(next)

class p(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        if self.key == other.key:
            return self.value < other.value
        else:
            return self.key < other.key

    ## 以下两种任意选
    def __str__(self):
        return str(self.key) + " " + str(self.value)
    #def __repr__(self):
    #    return "(" + str(self.key) + " , " + str(self.value) + ")"

def cust_pq2():
    heap = PriorityQueue()
    n1 = p(1, 5)
    n2 = p(1, 3)
    n3 = p(2, 2)
    n4 = p(2, 1)
    heap.put(n1)
    heap.put(n2)
    heap.put(n3)
    heap.put(n4)

    while not heap.empty():
        print(heap.get())

if __name__ == '__main__':
    cust_pq1()
