iteration = 0
iteration2 = 0
matrix = []
while True:
    try:
        temp_list = list(map(str,input().split()))
    except EOFError:
        break
    if temp_list == []:
        break
    matrix.append(temp_list)
while iteration < len(matrix):
    while iteration2 < len(matrix):
        pass
    