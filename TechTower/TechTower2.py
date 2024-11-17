def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def dfs(graph, start, exits=None):
    stack = []
    visited = [False] * len(graph)
    path = []
    
    stack.append(start)
    
    while stack:
        current = stack.pop()
        
        if not visited[current]:
            visited[current] = True
            path.append(current + 1)

            if exits and (current + 1) in exits: 
                return path

            
            neighbors = [i for i in range(len(graph[current])) if graph[current][i] == 1 and not visited[i]]
            neighbors = quicksort(neighbors)  
            
            for neighbor in reversed(neighbors):  
                stack.append(neighbor)
    if exits:
        return None
    else:
        return path

def evacuation_plan(n, k, m, adjacency_matrix, exits, threats):
    exits = quicksort(exits)
    threats = quicksort(threats)

    results = []
    safe = True
    
    for threat in threats:
        start_room = threat - 1  
        result_path = dfs(adjacency_matrix, start_room, exits)

        if result_path is None:
            results.append(f"BRAK DROGI Z POMIESZCZENIA {threat}")
            safe = False
        else:
            results.append(" ".join(map(str, result_path)))
    if safe:
        
        full_dfs_path = dfs(adjacency_matrix, threats[0] - 1)
        full_dfs_path = list(dict.fromkeys(full_dfs_path))
        if len(full_dfs_path) != len(adjacency_matrix):
            safe = False
        results.append(" ".join(map(str, full_dfs_path)))

    return safe, results

def validate_input(n, k, m, adjacency_matrix, exits, threats):
    if not (2 <= n <= 30) or not (1 <= k <= 5) or not (1 <= m <= 3):
        return False

    if len(adjacency_matrix) != n or any(len(row) != n for row in adjacency_matrix):
        return False

    if len(exits) != k or len(threats) != m:
        return False

    if not all(1 <= exit <= n for exit in exits) or not all(1 <= threat <= n for threat in threats):
        return False
    for row in adjacency_matrix:
        for element in row:
            if element not in (0, 1): 
                return False
    
    return True

if __name__ == "__main__":
    try:
        first_line = input().split()
        n = int(first_line[0])
        k = int(first_line[1])
        m = int(first_line[2])
        matrix = []
        for iteration in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        exits = list(map(int, input().split()))
        threats = list(map(int, input().split()))

        if validate_input(n, k, m, matrix, exits, threats):
            safe, results = evacuation_plan(n, k, m, matrix, exits, threats)
            if safe:
                print("BEZPIECZNY")
            else:
                print("NIEBEZPIECZNY")
            for line in results:
                print(line)
        else:
            print("BŁĄD")
            exit()

    except Exception:
        print("BŁĄD")
        



