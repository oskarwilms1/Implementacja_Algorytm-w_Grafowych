adjacency_list = []
adjacency_dic = {}
connected = True
while True:
    try:
        temp_list = list(map(str,input().split()))
    except EOFError:
        break
    if temp_list == []:
        break
    adjacency_list.append(temp_list)
chosen_vert = adjacency_list.pop()[0]
#create adjacency dict
NrOfVertices = len(adjacency_list)
if int(chosen_vert) not in range(1,NrOfVertices+1):
    print("BŁĄD")
    exit()
for iteration in range (1,NrOfVertices+1):
    adjacency_dic.update({iteration : adjacency_list[iteration-1][1:]})

visited = set()  # To keep track of visited nodes
stack = [chosen_vert]  
order = []       

while stack:
    vertex = stack.pop()  # Get the last vertex from the stack
    if vertex not in visited:
        visited.add(vertex)  # Mark vertex as visited
        order.append(vertex)  # Add vertex to the order of traversal
        
        # Process neighbors in reverse order to maintain the correct DFS order
        for neighbor in reversed(adjacency_dic.get(int(vertex), [])):
            if neighbor not in visited:  # Only add not visited neighbors
                stack.append(neighbor)
if len(order) == NrOfVertices:
    print("Porządek DFS:", ' '.join(map(str, order)))
    print("Graf jest spójny")
else:
    print("Graf jest niespójny")