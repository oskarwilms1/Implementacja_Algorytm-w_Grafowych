"""Napisz program, który dla danego ciągu liczb S, utworzy graf, którego wierzchołkami będą liczby ze zbioru S, natomiast krawędziami zbiór par (u,v)(u,v) takich że ∣u−v∣∈S∣u−v∣∈S.
Wyświetl macierz sąsiedztwa tego grafu.
Uwaga. Ciągi ze zbioru S mogą być nie posortowane.
Nie zmieniajmy kolejności występowania wierzchołków. 
Czyli traktujemy jako pierwszy wierzchołek, ten który występuje pierwszy w ciągu liczb S."""

Vertices = list(map(str,input().split()))
Edges = []
iteration = 0

while iteration <= len(Vertices)-2:
    iteration2 = iteration + 1
    while iteration2 <= len(Vertices)-1:
        if str(abs(int(Vertices[iteration]) - int(Vertices[iteration2]))) in Vertices:
            Edges.append(str(iteration)+','+str(iteration2))
        iteration2 += 1
    iteration += 1

length = len(Vertices)
matrix = [['0' for space in range(length)] for rows in range(length)]
iteration = 0
while iteration < len(Edges):
    temp_list = Edges[iteration].split(',')
    x = int(temp_list[0])
    y = int(temp_list[1])
    matrix[x][y] = '1'
    matrix[y][x] = '1'
    iteration += 1
for row in matrix:
    print(' '.join(row))





#print(Vertices)
