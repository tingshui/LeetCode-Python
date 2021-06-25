class TreeNode(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        
    def build(self, node_list):
        for node in node_list:
            self.insert(node)
    
    def insert(self, node):
        cur = self.root
        p = None
        while cur:
            p = cur
            if node.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        node.parent = p
        if p is None:
            self.root = node
        elif node.value < p.value:
            p.left = node
        else:
            p.right = node
            
    def search(self, value):
        cur  = self.root
        while cur:
            if cur.value == value:
                return cur
            elif cur.value > value:
                cur = cur.left
            else:
                cur = cur.right
        return None
            
    def preorder_print(self, node):
        if node is not None:
            print(node.value)
            self.preorder_print(node.left)
            self.preorder_print(node.right)
            
    def tree_min(self, cur):
        while cur.left is not None:
            cur = cur.left
        return cur
            
    def tree_successor(self, value):
        node = self.search(value)
        if node is None:
            return None
        if node.right:
            return self.tree_min(node.right)
        p = node.parent
        while p and node == p.right:
            node = p
            p = p.parent
        return p
            
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent           
            
    def delete(self, value):
        node = self.search(value)
        if node is None:
            return None
        if node.right is None:
            self.transplant(node, node.left)
        if node.left is None:
            self.transplant(node, node.right)
        else:
            p = self.tree_min(node.right)
            if p.parent != node:
                self.transplant(p, p.right)
                p.right = node.right
                p.right.parent = p
            self.transplant(node, p)
            p.left = node.left
            p.left.parent = p
        


def test():
    varList = [24,34,5,4,8,23,45,35,28,6,29]
    nodeList = [TreeNode(var) for var in varList]
    bst = BinarySearchTree()
    bst.build(nodeList)
    bst.preorder_print(bst.root)
    print(bst.search(5).value)
    print(bst.tree_min(bst.root).value)
    print(bst.tree_successor(5).value)
    bst.delete(5)
    bst.preorder_print(bst.root)

            

if __name__ == '__main__':
    test()



