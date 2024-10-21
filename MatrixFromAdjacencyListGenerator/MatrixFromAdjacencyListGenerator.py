iteration = 0
iteration2 = 0
matrix = []
adjacency_list = []
while True:
    try:
        temp_list = list(map(str,input().split()))
    except EOFError:
        break
    if temp_list == []:
        break
    matrix.append(temp_list)
while iteration < len(matrix):
    temp_list = []
    iteration2 = 0
    while iteration2 < len(matrix):
        if matrix[iteration][iteration2] == '1':
           temp_list.append(" "+str(iteration2+1))
        iteration2 += 1 
    adjacency_list.append(temp_list)
    iteration +=1
iteration = 0
while iteration < len(matrix):
    print(str(iteration+1)+''.join(adjacency_list[iteration]))
    iteration +=1
