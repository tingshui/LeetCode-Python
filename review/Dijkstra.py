import sys
from queue import PriorityQueue
# 是从以上最短距离数组中每次选择一个最近的点，将其作为下一个点，然后重新计算从起始点经过该点到其他所有点的距离，更新最短距离数据。
# 已经选取过的点就是确定了最短路径的点，不再参与下一次计算。
class Graph(object):
    def __init__(self, vertices):
        self.numV = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Dijkstra min distance from Source node")
        for node in range(self.numV):
            print("to node", node, "is: ", dist[node])

    
    def minDistance(self, dist, visited):
        min = sys.maxsize
        for v in range(self.numV):
            if dist[v] < min and visited[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    # version 1: V is vertices, E is edges
    # running time: O(V^2). Insert and Decrease-key takes O(1) time. Each minExtract takes O(V) because
    # we have to search through the heap. The second for loop function will take O(E) in total. So total running time is O(V^2 + E) = O(V^2)
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.numV
        dist[src] = 0
        visited = [False] * self.numV
        for count in range(self.numV):
            u = self.minDistance(dist, visited)
            visited[u] = True
            for v in range(self.numV):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)

    # version implemented with priority queue. https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
    # Running time is O(ElogE + E)
    # while loop will take at most E iteration. The min extract of priority queue is O(logE). The for loop will
    # take E times in total.
    def dijkstra_priorityqueue(self, src):
        # As it is hard to search in priority queue, so it is inefficient to update priority queue.
        # So we maintain - a list to record the min distance, and - a priority queue
        # When the distance to a vertex that is already in the queue is reduced, we wish to update the 
        # distance and thereby give it a different priority. We accomplish this by just adding another entry 
        # to the priority queue for the same vertex. (We also include a check after removing an entry from the
        # priority queue, in order to make sure that we only process each vertex once.)
        dist = [sys.maxsize] * self.numV
        dist[src] = 0

        # (key, value), distance should be key
        dist_pq = PriorityQueue()
        dist_pq.put((0, src))

        visited = set()
        while dist_pq.qsize() > 0:
            min_dist, min_vertices = dist_pq.get()
            # min_dist > dist[min_vertices] means not latest distance values, should already updated
            if min_dist > dist[min_vertices]:
                continue
            visited.add(min_vertices)
            for v in range(self.numV):
                new_dist = min_dist + self.graph[min_vertices][v]
                if self.graph[min_vertices][v] > 0 and v not in visited and dist[v] > new_dist:
                    dist[v] = new_dist
                    dist_pq.put((new_dist, v))
        self.printSolution(dist)

    # Step 2: Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    def Bellmanford(self, src):
        dist = [sys.maxsize] * self.numV
        dist[src] = 0
        for _ in range(self.numV - 1):
            # loop through all vertices
            for fromv in range(self.numV):
                 for tov in range(self.numV):
                     if self.graph[fromv][tov] != 0 and dist[tov] > dist[fromv] + self.graph[fromv][tov]:
                         dist[tov] = dist[fromv] + self.graph[fromv][tov]


        for fromv in range(self.numV):
            for tov in range(self.numV):
                if self.graph[fromv][tov] > 0 and dist[tov] > dist[fromv] + self.graph[fromv][tov]:
                    return False
        return True


def test():
    g = Graph(5)
    g.graph = [[0, 2, -5, 0, 0],
               [2, 0, 3, 0, 0],
               [-5, 3, 0, 7, 0],
               [0, 0, 7, 0, 9],
               [0, 0, 0, 9, 0]]

    #g.dijkstra(0)
    #g.dijkstra_priorityqueue(0)
    print(g.Bellmanford(0))



if __name__ == '__main__':
    test()

