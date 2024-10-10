import math
matrix = []
temp_matrix = []
is_directed = "Graf jest nieskierowany"
iteration = 0
length = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == '':
        break
    matrix.append(line)
matrix = ' '.join(matrix).split()
length = int(math.sqrt(len(matrix)))
for i in range(length*length+1):
    if i % length != 0 or i == 0:
        temp_matrix.append(matrix[i])
    else:
        matrix.append(temp_matrix)
        temp_matrix = []
        temp_matrix.append(matrix[i])
for i in range(length*length):
    matrix.pop(0)
while iteration < len(matrix):
    iteration2 = 0 
    while iteration2 < len(matrix):
        if matrix[iteration][iteration2] != matrix[iteration2][iteration]:
            is_directed = "Graf jest skierowany"
        iteration2 += 1
    iteration += 1
print(is_directed)

