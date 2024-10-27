try:
    AdjacencyList = eval(input())
except SyntaxError:
    exit(1)

NumberOfQueries = int(input())
ConnectionQueries = []
NeighboursQueries = []

for iteration in range(NumberOfQueries):
    try:
        user_input = input()
    except EOFError:
        break
    temp_list = user_input.split(' ')
    if temp_list[0] == 'neighbours':
        NeighboursQueries.append(temp_list[1])
    elif temp_list[0] == 'connection':
        if len(temp_list) != 3:
            continue
        ConnectionQueries.append(temp_list[1])
        ConnectionQueries.append(temp_list[2])

for element in NeighboursQueries:
    try:
        node_index = int(element)
        print(len(AdjacencyList.get(node_index, [])))
    except ValueError:
        exit(1)

iteration = 0
while iteration < len(ConnectionQueries):
    try:
        node1 = int(ConnectionQueries[iteration])
        node2 = int(ConnectionQueries[iteration + 1])
        if node2 in AdjacencyList.get(node1, []):
            print("Yes")
        else:
            print("No")
    except (ValueError, IndexError):
        exit(1)
    iteration += 2