matrix = []
last_line = None
def GetInput():
    first_line = list(map(int,input().split()))
    matrix.append(first_line)
    length = len(first_line)
    for i in range(0,length-1):
        user_input = list(map(int,input().split()))
        matrix.append(user_input)
    last_line = int(input())
    
def dijkstra():
    pass

GetInput()
print(matrix,last_line)