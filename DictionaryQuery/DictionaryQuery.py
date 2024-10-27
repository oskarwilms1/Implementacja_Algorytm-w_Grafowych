AdjacencyList = eval(input())
NumberOfQueries = int(input())
ConnectionQueries = []
NeighboursQueries = []

for iteration in range(0,NumberOfQueries):
    user_input = input()
    temp_list = user_input.split(' ')
    if temp_list[0] == 'neighbours':
        NeighboursQueries.append(temp_list[1])
    elif temp_list[0] == 'connection':
        ConnectionQueries.append(temp_list[1])
        ConnectionQueries.append(temp_list[2])
for element in NeighboursQueries:
    print(len(AdjacencyList[int(element)]))
iteration = 0
while iteration < len(ConnectionQueries)/2:
    if int(ConnectionQueries[iteration]) in AdjacencyList[iteration+1]:
        print("Yes")
    else:
        print("No")
    iteration +=1
