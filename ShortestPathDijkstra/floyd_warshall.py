def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j] if graph[i][j] > 0 else float('inf')
        dist[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def find_peripheral_vertices(graph):
    n = len(graph)
    # Getting the shortest paths between all pairs of vertices
    dist = floyd_warshall(graph)
    
    # Calculate the diameter of the graph
    diameter = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf'):
                diameter = max(diameter, dist[i][j])

    peripheral_vertices = []
    
    # Find all peripheral vertices
    for i in range(n):
        max_distance = max(dist[i])
        if max_distance == diameter:
            peripheral_vertices.append(i + 1)  # Adding 1 for 1-based index
    
    return sorted(peripheral_vertices)

def main():
    # Read the adjacency matrix
    input_data = []
    while True:
        try:
            line = input().strip()
            if line == '':
                break
            row = list(map(int, line.split()))
            input_data.append(row)
        except EOFError:
            break

    # The input_data is the adjacency matrix
    peripheral_vertices = find_peripheral_vertices(input_data)

    # Print the peripheral vertices
    print(" ".join(map(str, peripheral_vertices)))

if __name__ == "__main__":
    main()
