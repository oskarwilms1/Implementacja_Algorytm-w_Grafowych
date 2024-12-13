class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __lt__(self, other):
        if self.weight == other.weight:
            return (self.u, self.v) > (other.u, other.v)
        return self.weight > other.weight

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []
        self.adj_list = [[] for _ in range(n + 1)]

    def add_edge(self, a, b, w):
        self.edges.append((a, b, w))
        self.adj_list[a].append((b, w))
        self.adj_list[b].append((a, w))
    def dijkstra(self):
        dist = [[float('inf')] * (self.n + 1) for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            dist[i][i] = 0
            visited = [False] * (self.n + 1)
            min_edges = [(0, i)]  # (cost, vertex)

            while min_edges:
                current_dist, node = min_edges.pop(0)
                if visited[node]:
                    continue
                visited[node] = True

                for neighbor, weight in self.adj_list[node]:
                    distance = current_dist + weight
                    if distance < dist[i][neighbor]:
                        dist[i][neighbor] = distance
                        min_edges.append((distance, neighbor))
                min_edges.sort()  # Sort edges based on distance
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
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[largest]:
        largest = left

    if right < n and arr[right] < arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
def kruskal(n, edges):
    heap_sort(edges)  # Sort edges by weight and then by endpoints
    uf = UnionFind(n + 1)
    mst = []
    total_cost = 0

    for edge in edges:
        if uf.find(edge.u) != uf.find(edge.v):
            uf.union(edge.u, edge.v)
            mst.append(edge)
            total_cost += edge.weight

    return mst, total_cost



def main():
    first_line = input().split()
    n = int(first_line[0])  # liczba węzłów
    m = int(first_line[1])  # liczba krawędzi
    input_data = []
    for number in range(m):
        user_input = list(map(str, input().split()))
        sorted_input = [str(min(int(user_input[0]),int(user_input[1]))),str(max(int(user_input[0]),int(user_input[1]))),user_input[2]]
        input_data.append(sorted_input) 

    graph = Graph(n)

    edges = []
    for line in input_data:
        u, v, w = map(int, line)
        edges.append(Edge(u, v, w))
        graph.add_edge(u, v, w)

    mst, total_cost = kruskal(n, edges)

    # Wyniki

    print("SIEĆ PODSTAWOWA (MST):")
    heap_sort(mst)
    for edge in mst:
        print(f"{edge.u}-{edge.v}: {edge.weight}")
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