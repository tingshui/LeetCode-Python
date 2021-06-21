# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Stack(object):
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if self.is_empty():
            return
        else:
            return self.items[len(self.items)-1]
    
    def push(self, value):
        return self.items.append(value)
    
    def pop(self):
        if self.is_empty():
            return 
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)        

def test():
    S = Stack()
    print('栈是否为空：', S.is_empty())
    print("压栈'2'")
    S.push(2)
    print('栈顶为：', S.peek())
    print("压栈'3'")
    S.push(3)
    print("栈顶为：", S.peek())
    print("出栈")
    S.pop()
    print("栈的大小：", S.size())            
        
if __name__ == '__main__':
    test()
    

