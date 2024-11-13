def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def dfs(graph, start, exits, visited, path):
    visited[start] = True
    path.append(start + 1)  # Przechowujemy jako 1-indeksowane

    if (start + 1) in exits:
        return path  # Znaleziono wyjście, zwracamy ścieżkę

    # Sprawdzanie sąsiadów
    neighbors = [i for i in range(len(graph[start])) if graph[start][i] == 1 and not visited[i]]
    neighbors = quicksort(neighbors)  # Sortowanie sąsiadów

    for neighbor in neighbors:
        result_path = dfs(graph, neighbor, exits, visited, path)
        if result_path is not None:
            return result_path

    path.pop()  # Backtrack
    return None  # Nie znaleziono drogi

def full_dfs(graph, start, visited, path):
    visited[start] = True
    path.append(start + 1)  # Przechowujemy jako 1-indeksowane

    # Sprawdzanie sąsiadów
    neighbors = [i for i in range(len(graph[start])) if graph[start][i] == 1 and not visited[i]]
    neighbors = quicksort(neighbors)  # Sortowanie sąsiadów

    for neighbor in neighbors:
        full_dfs(graph, neighbor, visited, path)

def evacuation_plan(n, k, m, adjacency_matrix, exits, threats):
    exits = quicksort(exits)
    threats = quicksort(threats)

    results = []
    safe = True
    
    for threat in threats:
        visited = [False] * n
        path = []
        start_room = threat - 1  # Zmiana na indeks 0
        result_path = dfs(adjacency_matrix, start_room, exits, visited, path)

        if result_path is None:
            results.append(f"BRAK DROGI Z POMIESZCZENIA {threat}")
            safe = False
        else:
            results.append(" ".join(map(str, result_path)))
    
    if safe:
        # Oblicz pełną kolejność ewakuacji
        full_dfs_path = []
        visited_full = [False] * n
        full_dfs(adjacency_matrix, threats[0] - 1, visited_full, full_dfs_path)
        results.append(" ".join(map(str, full_dfs_path[:len(full_dfs_path)-1])))

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
    for element in exits:
        if element in threats:
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
        exit()




