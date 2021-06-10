# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class BinaryNode(object):
    
    def __init__(self, left_child, right_child, value):
        self._left_child = left_child
        self._right_child = right_child
        self._value = value
        
    @property
    def left_child(self):
        return self._left_child
    
    @property
    def right_child(self):
        return self._right_child
    
    @property
    def value(self):
        return self._value
    
    @left_child.setter
    def left_child(self, value):
        self._left_child = value
        
    @right_child.setter
    def right_child(self, value):
        self._right_child = value
        
    @value.setter
    def value(self, value):
        self._value = value
    
class BinaryTree(object):
    def __init__(self):
        self._root = None
        self._bi_list = [] # 使用队列存放二叉树的层次节点信息

    @property
    def root(self):
        return self._root

#二叉树的遍历
#深度优先遍历（Depth First Search，DFS）：沿着树的深度遍历树的节点，尽可能深的搜索树的分支。
#前序遍历：NLR，根结点->左子树->右子树；
#中序遍历：LNR，左子树->根结点->右子树；
#后续遍历：LRN，左子树->右子树->根结点。
#广度优先遍历（Breadth First Search，BFS；也叫层次遍历，level order）：是从根节点开始，沿着树的宽度遍历树的节点。如果所有节点均被访问，则算法中止。    

    # 依次为二叉树添加节点（从上至下，从左至右)
    def add(self, value):
        node = BinaryNode(None, None, value)
        if self._root is None:
            self._root = node
            self._bi_list.append(node)
        else:
            r = self._bi_list[0]
            self._bi_list.append(node)
            if r.left_child is None:
                r._left_child = node
            else:
                r._right_child = node
                self._bi_list.pop(0)


    ###################### Traversal ##########################
    # pre-order/in-order/post-order recursive
    def pre_order(self, root):
        if root is None:
            return 
        print(root.value)
        self.pre_order(root.left_child)
        self.pre_order(root.right_child)
        
    def pre_order_stack(self, root):
        if root is None:
            return
        stack = []
        node = root 
        while node or stack:
            while node:
                print(node.value)
                stack.append(node)
                node = node.left_child
            node = stack.pop()            
            node = node.right_child
        
    def in_order(self, root):
        if root is None:
            return        
        self.in_order(root.left_child)
        print(root.value)
        self.in_order(root.right_child)
    
    def in_order_stack(self, root):
        if root is None:
            return
        stack = []
        node = root 
        while node or stack:
            while node:               
                stack.append(node)
                node = node.left_child
            node = stack.pop()  
            print(node.value)
            node = node.right_child
    
    # Very interesting method, reverse adding nodes!
    # in-order non-recursive
    def in_order_stack_2(root):
        stack =[root]
        while stack:
            node = stack.pop(-1)
            if node:
                if isinstance(node, Node):
                    stack.append(node.right_child)
                    stack.append(node.value)               
                    stack.append(node.left_child)
                else:
                    print(node)


    def post_order(self, root):
        if root is None:
            return        
        self.post_order(root.left_child)       
        self.post_order(root.right_child)
        print(root.value)

    
    def post_order_stack(self, root):
        stack =[root]
        while stack:
            node = stack.pop(-1)
            if node:
                if isinstance(node, BinaryNode):
                    stack.append(node.value)
                    stack.append(node.right_child)
                    stack.append(node.left_child)
                else:
                    print(node)                   
        
                        
    def post_order_stack_2(self, root):
        if root is None:
            return
        stack1, stack2 = [], []
        stack1.append(root)
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left_child:
                stack1.append(node.left_child)
            if node.right_child:
                stack1.append(node.right_child)
        for i in stack2[::-1]:
            print(i.value)
                      
    
    def level_order(self, root):
        if root is None:
            return
        queue =[root]
        while queue:
            node = queue.pop(0)
            print(node.value)
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)                
         


##################### other tree properties ######################
############## count the number of nodes
def node_count(root):
    if root:
        #print(root.value)
        return 1 + node_count(root.left_child) + node_count(root.right_child)
    else:
        return 0
# non recursive version is similar to traversal
def node_count_non(root):
    return len(levelorder(root))

################ tree depth
def tree_depth(root):
    if root is None:
        return 0
    else:
        return 1 + max(tree_depth(root.left_child), tree_depth(root.right_child))


def tree_depth_non(root):
    if root is None:
        return 0
    queue = [root]
    depth = 0
    while(True):
        if (len(queue) == 0):
            return depth
        node_count = len(queue)        
        depth += 1
        while (node_count > 0):
            node = queue.pop(0)
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)
            node_count -= 1
        
################# tree leaves
def tree_leaves(root):
    if root is None:
        return 0
    if root.right_child is None and root.left_child is None:
        return 1
    return tree_leaves(root.right_child) + tree_leaves(root.left_child)

def test():
    BT = BinaryTree()
    print('依次为二叉树添加10个节点...')
    for i in range(7):
        BT.add(i + 1)
    print('前序遍历')
    BT.pre_order(BT.root)
    print('中序遍历')
    BT.in_order(BT.root)
    print('后序遍历')
    BT.post_order(BT.root)
    print('前序遍历，非递归方式')
    BT.pre_order_stack(BT.root)
    print('中序遍历，非递归方式')
    BT.in_order_stack(BT.root)
    print('后序遍历，非递归方式')
    BT.post_order_stack_2(BT.root)
    print('层次遍历')
    BT.level_order(BT.root)

            
        
if __name__ == '__main__':
    test()
    
