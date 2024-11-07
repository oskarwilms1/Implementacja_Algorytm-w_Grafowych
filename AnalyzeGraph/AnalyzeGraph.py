def HandleUserInput():
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
    count = 0
    for row in matrix:
        for element in row:
            if element != '0':
                count +=1

adjacency_list = HandleUserInput()
Matrix = ConvertToMatrix(adjacency_list)
print("Ilość wierzchołków: ",CountVertices(Matrix))
CountEdges(Matrix)