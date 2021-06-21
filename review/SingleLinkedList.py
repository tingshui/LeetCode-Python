class SingleListNode(object):
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class SingleLinkedList(object):
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    # add the node to the front of linkedlist
    def add(self, value):
        newNode = SingleListNode(value, self.head)
        self.head = newNode
    
    # add the node to the end of the linkedlist
    def append(self, value):
        newNode = SingleListNode(value)
        cur = self.head
        if cur is None:
            self.head = newNode
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
    
    # insert after pos
    def insert(self, pos, value):
        if pos <= 0:
            self.add(value)
        elif pos > self.length() -1:
            self.append(value)
        else:
            newNode = SingleListNode(value)
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
    
    def remove(self, value):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.value == value:
                if pre is None:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                cur =cur.next
            else:
                pre = cur
                cur = cur.next
    
    def length(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count
            
    def search(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        
    def travel(self):
        cur = self.head
        ls = []
        while cur is not None:
            ls.append(cur.value)
            cur = cur.next
        return ls
            
        
def test():
    SL = SingleLinkedList()
    print('单链表是否为空：', SL.is_empty())
    SL.add(1)
    SL.add(2)
    SL.append(5)
    print('单链表为：', SL.travel())
    SL.insert(2, 3)
    print('单链表中是否有4：', SL.search(4))
    print('单链表为：', SL.travel())
    print('单链表长度：', SL.length())
    SL.remove(2)
    print('单链表为：', SL.travel())


if __name__ == '__main__':
    test()




