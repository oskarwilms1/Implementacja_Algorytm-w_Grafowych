"""Napisz program, który utworzy graf skierowany dla ciągów liczb SS i AA o następującej definicji:

    Zbiorem wierzchołków grafu będą liczby, które należą do ciągu AA
    Istnieje łuk (x,y)(x,y), jeśli x≠yx=y oraz y−x∈Sy−x∈S.

Graf przedstaw w postaci macierzy sąsiedztwa.

Pierwszy wiersz na wejściu jest to ciąg AA, natomiast drugi wiersz reprezentuje ciąg SS.

Uwaga. Ciągi ze zbioru A mogą być nie posortowane. Nie zmieniajmy kolejności występowania wierzchołków. Czyli traktujemy jako pierwszy wierzchołek, ten który występuje pierwszy w ciągu liczb AA."""

Vertices = list(map(str,input().split()))
Sequence = list(map(str,input().split()))
Edges = []
iteration = 0
length = len(Vertices)
while iteration < length:
    iteration2 = 0
    while iteration2 < length:
        if str(int(Vertices[iteration2]) - int(Vertices[iteration])) in Sequence:
            Edges.append(str(iteration)+','+str(iteration2))
        iteration2 += 1
    iteration += 1

matrix = [['0' for space in range(length)] for rows in range(length)]
iteration = 0
while iteration < len(Edges):
    temp_list = Edges[iteration].split(',')
    x = int(temp_list[0])
    y = int(temp_list[1])
    matrix[x][y] = '1'
    iteration += 1
for row in matrix:
    print(' '.join(row))






