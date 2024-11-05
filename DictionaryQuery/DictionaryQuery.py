AdjacencyList = eval(input())
NumberOfQueries = int(input())
ConnectionQueries = []
NeighboursQueries = []
Queue = []

iteration2 = 0

for iteration in range(0,NumberOfQueries):
    try:
        user_input = input()
    except EOFError:
        break 
    temp_list = user_input.split(' ')
    if temp_list[0] == 'neighbours':
        NeighboursQueries.append(temp_list[1])
        Queue.append("N")
    elif temp_list[0] == 'connection':
        ConnectionQueries.append(temp_list[1])
        ConnectionQueries.append(temp_list[2])
        Queue.append("C")
iteration = 0
for element in Queue:
    if element == "N":
        print(len(AdjacencyList[int(NeighboursQueries[iteration])]))
        iteration += 1
    if element == "C":
        if int(ConnectionQueries[iteration2]) in AdjacencyList[int(ConnectionQueries[iteration2+1])]:
            print("Yes")
        else:
            print("No")
        iteration2 += 2

