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

while iteration <= len(Vertices)-2:
    iteration2 = 0
    while iteration2 <= len(Vertices)-1:
        if str(int(Vertices[iteration2]) - int(Vertices[iteration])) in Vertices:
            Edges.append(str(iteration2)+','+str(iteration))
        iteration2 += 1
    iteration += 1
print(Edges)







