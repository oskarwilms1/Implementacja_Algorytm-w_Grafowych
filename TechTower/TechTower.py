first_line = input().split()
nr_of_rooms = int(first_line[0])
nr_of_ev_rooms = int(first_line[1])
nr_of_danger_rooms = int(first_line[2])

if len(first_line) == 3:
    if nr_of_rooms in range (2,31) and nr_of_ev_rooms in range (1,6) and nr_of_danger_rooms in range (1,4):
        pass
    else:
        print("BŁĄD")
        exit()
else:
    print("BŁĄD")
    exit()

matrix = []
for iteration in range(nr_of_rooms):
    row = list(map(int, input().split()))
    matrix.append(row)
try:
    evacuate_rooms = input().split()
except EOFError:
    print("BŁĄD")
    exit()

if len(evacuate_rooms) != nr_of_ev_rooms:
    print("BŁĄD")
    exit()

try:
    danger_rooms = input().split()
except EOFError:
    print("BŁĄD")
    exit()

if len(danger_rooms) != nr_of_danger_rooms:
    print("BŁĄD")
    exit()
for element in danger_rooms:
    if element in evacuate_rooms:
        print("BŁĄD")
        exit()

list_of_routs = []

for element in danger_rooms:
    order = [element]
    visited = [False] * nr_of_rooms
    stack = [int(element) - 1]  
    visited[int(element) - 1] = True
    is_eva = False
    while stack:
        vertex = stack.pop()
        for neighbor in range(nr_of_rooms):
            if matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                order.append(str(neighbor+1))
                break
        for element in order:
            if element in evacuate_rooms:
                is_eva = True
        if is_eva:
            list_of_routs.append(order)
            break
    
starting_room = int(danger_rooms[0])
order = [str(starting_room)]
visited = [False] * nr_of_rooms
stack = [starting_room-1]  
visited[starting_room-1] = True
while stack:
    vertex = stack.pop()
    for neighbor in range(nr_of_rooms):
        if matrix[vertex][neighbor] == 1 and not visited[neighbor]:
            visited[neighbor] = True
            stack.append(neighbor)
            order.append(str(neighbor+1))
            break
final_route = order
if len(list_of_routs) == nr_of_danger_rooms and len(final_route) == nr_of_rooms:
    print("BEZPIECZNY")
    for route in list_of_routs:
        print(' '.join(route))
    print(' '.join(final_route))
else:
    print("NIEBEZPIECZNY")
    for route in list_of_routs:
        print(' '.join(route))
    for number in range(len(list_of_routs)+1,len(danger_rooms)+1):
        print("BRAK DROGI Z POMIESZCZENIA",danger_rooms[number-1])


