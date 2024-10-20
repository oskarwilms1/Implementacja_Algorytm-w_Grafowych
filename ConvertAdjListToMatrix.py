adjacency_list = {}
matrix = []
temp_matrix = []
length = 0
iteration = 0
while True:
    try:
        temp_list = list(map(str,input().split()))
    except EOFError:
        break
    if temp_list == []:
        break
    adjacency_list.update({temp_list[0]: temp_list[1:]})
    length +=1
while iteration < length:
    iteration2 = 1
    temp_matrix = []
    while iteration2 <= length:
        if str(iteration2) in adjacency_list[str(iteration+1)]:
            temp_matrix.append("1")
        else:
            temp_matrix.append("0")
        iteration2 +=1
    matrix.append(temp_matrix)
    iteration+=1
for row in matrix:
    print(' '.join(row))
