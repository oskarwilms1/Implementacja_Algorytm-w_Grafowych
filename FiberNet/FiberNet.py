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

def dfs(u, graph, visited, component):
    visited[u] = True
    component.append(u)
    heap_sort(graph[u])
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited, component)

def find_bridges_and_components(n, edges):
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge.u].append(edge.v)
        graph[edge.v].append(edge.u)

    vis = [False] * (n + 1)
    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    parent = [-1] * (n + 1)
    bridges = []
    time = [0]

    def bridge_dfs(u):
        vis[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        for v in sorted(graph[u]):
            if not vis[v]:
                parent[v] = u
                bridge_dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:  # if u-v is a bridge
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for i in range(1, n + 1):
        if not vis[i]:
            bridge_dfs(i)

    # Create a graph without bridges for finding components
    graph_without_bridges = [[] for _ in range(n + 1)]
    bridge_set = set(bridges)
    
    for edge in edges:
        if (edge.u, edge.v) not in bridge_set and (edge.v, edge.u) not in bridge_set:
            graph_without_bridges[edge.u].append(edge.v)
            graph_without_bridges[edge.v].append(edge.u)

    # Find components
    visited = [False] * (n + 1)
    components = []

    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(i, graph_without_bridges, visited, component)
            components.append(sorted(component))

    bridges.sort(key=lambda x: int(x[0]))

    return bridges, components


def main():
    first_line = input().split()
    n = int(first_line[0])  # liczba węzłów
    m = int(first_line[1])  # liczba krawędzi
    input_data = []
    for number in range(m):
        user_input = list(map(str, input().split()))
        sorted_input = [str(min(int(user_input[0]),int(user_input[1]))),str(max(int(user_input[0]),int(user_input[1]))),user_input[2]]
        input_data.append(sorted_input) 


    edges = []
    for line in input_data:
        u, v, w = map(int, line)
        edges.append(Edge(u, v, w))

    mst, total_cost = kruskal(n, edges)
    bridges, components = find_bridges_and_components(n, edges)

    # Wyniki

    print("MINIMALNE DRZEWO SPINAJĄCE:")
    heap_sort(mst)
    for edge in mst:
        print(f"{edge.u} {edge.v} {edge.weight}")
    print(f"Łączny koszt: {total_cost}")

    print("\nMOSTY:")
    if bridges:
        for u, v in bridges:
            print(f"{u} {v}")
    else:
        print("BRAK MOSTÓW")

    print("\nKOMPONENTY:")
    print(f"{len(components)} KOMPONENTY:", end=" ")
    components_str = ' '.join(f"[{' '.join(map(str, comp))}]" for comp in components)
    print(components_str)

if __name__ == "__main__":
    main()