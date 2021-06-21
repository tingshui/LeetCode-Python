class DoubleListNode(object):
    """双向节点类"""
    def __init__(self, _item, _prev=None, _next=None):
        self.item = _item
        self.prev = _prev
        self.next = _next

class DoubleLinkedList(SingleLinkedList):
    """双向链表类，继承单链表类"""
    def __init__(self):
        self.head = None

    def add(self, newdata):
        node = DoubleListNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, newdata):
        node = DoubleListNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, newdata):
        if pos <= 0:
            self.add(newdata)
        elif pos > self.length() - 1:
            self.append(newdata)
        else:
            node = DoubleListNode(newdata)
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def remove(self, olddata):
        """删除一个指定的节点"""
        if self.is_empty():
            return
        elif self.head.item == olddata:
            if self.head.next is None:
                self.head = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.item == olddata:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                    return
                cur = cur.next
            if cur.item == olddata:
                cur.prev.next = None

def test_DL():
    DL = DoubleLinkedList()
    print('双向链表是否为空：', DL.is_empty())
    DL.add(1)
    DL.add(2)
    DL.append(5)
    print('双向链表为：', DL.travel())
    print("在第二个节点之后插入节点'3'")
    DL.insert(2, 3)
    print('双向链表为：', DL.travel())
    print('双向链表中是否有4：', DL.search(4))
    print('双向链表长度：', DL.length())
    print("删除节点'1'")
    DL.remove(1)
    print('双向链表为：', DL.travel())

if __name__ == '__main__':
    test()

