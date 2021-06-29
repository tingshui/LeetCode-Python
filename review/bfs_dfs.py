# the reason for using defaultdict: if using dict, we will get
# key error when the inserted key is not available, defaultdict will
# directly add the new key. Defaultdict is a sub-class of the dict class
# that returns a dictionary-like object. The functionality of both 
# dictionaries and defualtdict are almost same except for the fact that 
# defualtdict never raises a KeyError. It provides a default value for 
# the key that does not exists.
from collections import defaultdict

def def_value():
    return("Not Present")

class Graph(object):
    def __init__(self):
        # Using List as default_factory.
        # default_factory: A function returning the default value for 
        # the dictionary defined. If this argument is absent then the
        # dictionary raises a KeyError.
        self.graph = defaultdict(list)
    
    def addEdge(self, fromV, toV):
        self.graph[fromV].append(toV)
        
    def BFS(self, s):
        # Notice, we cannot use len(g.graph), because vertice may 
        #  not be continuous
        visited = [False] * (max(self.graph) + 1)
        queue = [s]
        visited[s]= True
        while queue:
            s = queue.pop(0)
            # In Python 3, "end =' '" appends space instead of newline.
            print(s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    def DFSUtil(self, s, visited):
        visited.add(s)
        print(s, end = " ")
        for i in self.graph[s]:
            if i not in visited:
                self.DFSUtil(i, visited)
    
    def DFS(self, s):
        # use a set to store the visited items is easier
        visited = set()        
        self.DFSUtil(s, visited)


def test():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(5, 5)
    for x, y in g.graph.items():
        print(x, y)
    g.BFS(2)
    print("\n")
    g.DFS(2)


if __name__ == '__main__':
    test()



