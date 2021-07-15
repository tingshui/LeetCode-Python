# the reason for using defaultdict: if using dict, we will get
# key error when the inserted key is not available, defaultdict will
# directly add the new key. Defaultdict is a sub-class of the dict class
# that returns a dictionary-like object. The functionality of both
# dictionaries and defualtdict are almost same except for the fact that
# defualtdict never raises a KeyError. It provides a default value for
# the key that does not exists.
from collections import defaultdict

class Graph(object):
    def __init__(self):
        # Using List as default_factory.
        # default_factory: A function returning the default value for
        # the dictionary defined. If this argument is absent then the
        # dictionary raises a KeyError.
        self.graph = defaultdict(list)

    def addEdge(self, fromV, toV):
        self.graph[fromV].append(toV)

    ################# BFS
    def BFS(self, s):
        # Notice, we cannot use len(g.graph), because vertice may
        #  not be continuous
        visited = [False] * (max(self.graph) + 1)
        queue = [s]
        visited[s] = True
        while queue:
            s = queue.pop(0)
            # In Python 3, "end =' '" appends space instead of newline.
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # DFS
    def DFSUtil(self, s, visited):
        visited.add(s)
        print(s, end=" ")
        for i in self.graph[s]:
            if i not in visited:
                self.DFSUtil(i, visited)

    def DFS(self, s):
        # use a set to store the visited items is easier
        visited = set()
        self.DFSUtil(s, visited)

    ################### Topolgical order
    def TopologicalUtil(self, v, visited, result):
        visited.add(v)
        for i in self.graph[v]:
            if i not in visited:
                self.TopologicalUtil(i, visited, result)
        result.append(v)

    def Topologicalsort(self):
        visited = set()
        result = []
        for v in self.graph.keys():
            if v not in visited:
                self.TopologicalUtil(v, visited, result)
        print(result[::-1])

    ############ Strongly connected component detection
    def getTranspose(self):
        gt = Graph()
        for vertice, edge_list in self.graph.items():
            for edge in edge_list:
                gt.addEdge(edge, vertice)
        return gt

    def DFSUtil_order(self, s, visited, stack):
        visited.add(s)
        for i in self.graph[s]:
            if i not in visited:
                self.DFSUtil_order(i, visited, stack)
        stack = stack.append(s)

    def printSCCs(self):
        visited_order = set()
        stack_order = []
        for v in self.graph.keys():
            if v not in visited_order:
                self.DFSUtil_order(v, visited_order, stack_order)
        gr = self.getTranspose()
        visited = set()
        while stack_order:
            i = stack_order.pop()
            if i not in visited:
                gr.DFSUtil(i, visited)
                print(" ")

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
    print("bfs: ")
    g.BFS(2)
    print("\ndfs: ")
    g.DFS(2)
    print("\ntopological:")
    g.Topologicalsort()
    print("\nstrongly connected components:")
    g.printSCCs()



if __name__ == '__main__':
    test()



