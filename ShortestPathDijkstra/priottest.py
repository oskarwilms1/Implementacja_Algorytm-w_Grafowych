class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        self.elements.append((priority, item))

    def get(self):
        self.elements.sort()
        return self.elements.pop(0)[1]

import sys

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []
        self.adj_list = [[] for _ in range(n + 1)]
        self.parent = [i for i in range(n + 1)]

    def add_edge(self, a, b, w):
        self.edges.append((w, a, b))
        self.adj_list[a].append((b, w))
        self.adj_list[b].append((a, w))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

    def kruskal(self):
            mst_edges = []
            total_cost = 0
            pq = []
            for edge in self.edges:
                w, a, b = edge
                pq.append((w, a, b))
            pq.sort()

            while pq:
                w, a, b = pq.pop(0)
                if self.find(a) != self.find(b):
                    mst_edges.append([a, b, w])
                    total_cost += w
                    self.union(a, b)
            return mst_edges, total_cost

    def dijkstra(self, start):
        dist = [sys.maxsize] * self.n
        dist[start] = 0

        for _ in range(self.n):
            node = -1
            min_distance = sys.maxsize
            for i in range(self.n):
                if dist[i] < min_distance:
                    min_distance = dist[i]
                    node = i
            if min_distance == sys.maxsize:
                break

            for neighbor, weight in self.adj_list[node]:
                distance = dist[node] + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance

        return dist

    def find_articulation_points(self):
        ids = 0
        low = [0] * (self.n + 1)
        id = [-1] * (self.n + 1)
        visited = [False] * (self.n + 1)
        articulation_points = set()

        def dfs(at, parent):
            nonlocal ids
            visited[at] = True
            ids += 1
            id[at] = low[at] = ids

            children = 0
            for to, _ in self.adj_list[at]:
                if to == parent:
                    continue
                if not visited[to]:
                    children += 1
                    dfs(to, at)
                    low[at] = min(low[at], low[to])
                    if parent != -1 and low[to] >= id[at]:
                        articulation_points.add(at)
                else:
                    low[at] = min(low[at], id[to])

            if parent == -1 and children > 1:
                articulation_points.add(at)

        for i in range(1, self.n + 1):
            if not visited[i]:
                dfs(i, -1)
        
        return sorted(articulation_points)

def main():
    # Read the first line for n and m
    first_line = input().strip()
    n, m = map(int, first_line.split())
    
    if not (2 <= n <= 100 and n - 1 <= m <= n * (n - 1) // 2):
        print("BŁĄD")
        return

    graph = Graph(n)
    
    # Read each edge
    for _ in range(m):
        edge_line = input().strip()
        a, b, w = map(int, edge_line.split())
        graph.add_edge(a, b, w)

    # Calculate the MST
    mst_edges, total_cost = graph.kruskal()

    # Output MST
    print("SIEĆ PODSTAWOWA (MST):")
    for edge in mst_edges:
        if edge[0]>edge[1]:
            edge[0],edge[1]=edge[1],edge[0]
    mst_edges.sort(key=lambda x: (x[2],x[0]))
    for edge in mst_edges:
        print(f"{edge[0]}-{edge[1]}: {edge[2]}")
       
        
    print(f"Łączny czas: {total_cost}")

    # Calculate shortest paths
    distances = graph.dijkstra()

    # Calculate Diameter, Radius, Centers, and Peripheries
    diameter = 0
    eccentricities = []

    for i in range(1, n + 1):
        max_dist = max(distances[i][1:n + 1])
        eccentricities.append(max_dist)
        if max_dist > diameter:
            diameter = max_dist
    diameter = max(max(distances[i][1:n+1]) for i in range(1, n+1))
    radius = min(eccentricities)
    
    centers = [i for i in range(1, n + 1) if eccentricities[i - 1] == radius]
    periphery = [i for i in range(1, n + 1) if eccentricities[i - 1] == diameter]

    # Output parameters
    print("\nPARAMETRY SIECI:")
    print(f"Średnica: {diameter}")
    print(f"Promień: {radius}")
    print(f"Centrum: {centers}")
    print(f"Peryferium: {periphery}")

    # Output travel times
    print("\nCZASY PRZEJAZDÓW:")
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if distances[i][j] == float('inf'):
                row.append("INF")
            else:
                row.append(str(distances[i][j]))
        print(" ".join(row))

    articulation_points = graph.find_articulation_points()

    print("\nPUNKTY KRYTYCZNE:")
    if articulation_points:
        print(" ".join(map(str, articulation_points)))
    else:
        print("BRAK")

if __name__ == "__main__":
    main()