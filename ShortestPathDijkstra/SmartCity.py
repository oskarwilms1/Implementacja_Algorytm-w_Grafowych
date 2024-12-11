class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []
        self.adj_list = [[] for _ in range(n + 1)]

    def add_edge(self, a, b, w):
        self.edges.append((a, b, w))
        self.adj_list[a].append((b, w))
        self.adj_list[b].append((a, w))

    def prim(self):
        mst_edges = []
        total_cost = 0
        visited = [False] * (self.n + 1)
        min_edges = [(0, 1, -1)]  # (cost, vertex, parent)

        while min_edges:
            cost, node, parent = min_edges.pop(0)
            if visited[node]:
                continue
            visited[node] = True
            if parent != -1:
                mst_edges.append((parent, node, cost))
            total_cost += cost

            for neighbor, weight in self.adj_list[node]:
                if not visited[neighbor]:
                    min_edges.append((weight, neighbor, node))

            min_edges.sort()  # Sort edges based on weight
        return mst_edges, total_cost

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
    mst_edges, total_cost = graph.prim()

    # Output MST
    print("SIEĆ PODSTAWOWA (MST):")
    mst_edges.sort(key=lambda x: (x[2], x[0], x[1]))  # sort by weight, then by vertex
    for a, b, w in mst_edges:
        if a<b:
            print(f"{a}-{b}: {w}")
        else:
            print(f"{b}-{a}: {w}")
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