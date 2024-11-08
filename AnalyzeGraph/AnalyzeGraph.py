def SetAdjList():
    adjacency_list = {}
    while True:
        try:
            temp_list = list(map(str,input().split()))
        except EOFError:
            break
        if temp_list == []:
            break
        adjacency_list.update({temp_list[0]: temp_list[1:]})
    return adjacency_list
def ConvertToMatrix(adj_list : dict):
    Matrix = []
    length = len(adj_list)
    iteration = 0
    while iteration < length:
        iteration2 = 1
        temp_matrix = []
        while iteration2 <= length:
            if str(iteration2) in adj_list[str(iteration+1)]:
                temp_matrix.append("1")
            else:
                temp_matrix.append("0")
            iteration2 +=1
        Matrix.append(temp_matrix)
        iteration+=1
    return Matrix
def PrintMatrix(matrix : list):
    for row in matrix:
        print(' '.join(row))
def CountVertices(matrix):
    return len(matrix)
def CountEdges(matrix):
    Edges = 0
    for row in matrix:
        for element in row:
            if element != '0':
                Edges +=1
    return int(Edges/2)
def CountPowers(adj_list):
    Powers = []
    iteration = 1
    while iteration <= len(adj_list):
        Powers.append(str(len(adj_list[str(iteration)])))
        iteration += 1
    return Powers
def AveragePower(Powers):
    temp_list = [int(i) for i in Powers]
    result = sum(temp_list)/len(temp_list)
    result = str(format(result, '.2f'))
    return result
def IsGraphComplete(vert,edg):
    if edg == vert*(vert-1)/2:
        return True
    else:
        return False
def IsGraphCycle(vert,edg,powers):
    result = True
    if vert == edg:
        for element in powers:
            if element != '2':
                result = False
    else:
        result = False
    return result
def IsGraphPath(vert,edg,powers):
    result = True
    temp_list = powers
    countOfOnes=0
    if vert-1 == edg:
        for element in temp_list:
            if element == '1':
                temp_list.remove('1')
                countOfOnes += 1
        if countOfOnes == 2:
            for element in temp_list:
                if element != '2':
                    result = False
        else:
            result = False
    else:
        result = False
    return result
def IsGraphTree(vert,edg,powers):
    result = True
    if vert-1 == edg:
        if '0' in powers:
            result = False
    else:
        result = False
    return result
def IsGraphHyperCube(vert,edg,powers,matrix):
    if vert <= 0 or (vert & (vert-1)) != 0:
        return False
    dimention = 0
    temp = vert
    while temp > 1:
        temp //= 2
        dimention += 1
    if edg != dimention*(2**(dimention-1)):
        return False
    if powers != [str(dimention)] * vert:
        return False
    def is_connected(matrix):
        #DFS
        visited = [False] * vert
        stack = [0]  
        visited[0] = True

        while stack:
            vertex = stack.pop()
            for neighbor in range(vert):
                if matrix[vertex][neighbor] == '1' and not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return all(visited)
    if not is_connected(matrix):
        return False

    return True


adjacency_list = SetAdjList()
Matrix = ConvertToMatrix(adjacency_list)
ListOfPowers = CountPowers(adjacency_list)
Edges = CountEdges(Matrix)
Vertices = CountVertices(Matrix)
print("Ilość wierzchołków:",Vertices)
print("Ilość krawędzi:",Edges)
print("Stopnie wierzchołków: "+' '.join(ListOfPowers))
print("Średni stopień:",AveragePower(ListOfPowers))
if IsGraphComplete(Vertices,Edges) == True:
    print("Jest to graf pełny")
    if IsGraphCycle(Vertices,Edges,ListOfPowers) == True:
        print("Jest to cykl")
elif IsGraphCycle(Vertices,Edges,ListOfPowers) == True:
    print("Jest to cykl")
    if IsGraphHyperCube(Vertices,Edges,ListOfPowers,Matrix) == True:
        print("Jest to hiperkostka")
elif IsGraphHyperCube(Vertices,Edges,ListOfPowers,Matrix) == True:
    print("Jest to hiperkostka")
elif IsGraphTree(Vertices,Edges,ListOfPowers) == True:
    if IsGraphPath(Vertices,Edges,ListOfPowers) == True:
        print("Jest to ścieżka")
        print("Jest to drzewo")
    else:
        print("Jest to drzewo")
else:
    print("Graf nie należy do żadnej z podstawowych klas")
    
