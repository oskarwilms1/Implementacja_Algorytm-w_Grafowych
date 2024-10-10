matrix = []
count = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == '':
        break
    matrix.append(line)
Number_of_vertices = len(matrix)
matrix = list(' '.join(matrix).split())
for element in matrix:
    if element != '0':
        count +=1

print("Ilość wierzchołków: "+str(Number_of_vertices))
print("Ilość krawędzi: "+str(int(count/2)))



