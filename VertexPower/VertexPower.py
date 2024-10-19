adjacency_list = {}
count = 0
while True:
    try:
        temp_list = list(map(str,input().split()))
    except EOFError:
        break
    if temp_list == []:
        break
    adjacency_list.update({temp_list[0]: temp_list[1:]})
for element in adjacency_list:
    if isinstance(adjacency_list[element], list):
        count += len(list(adjacency_list[element]))
print(round(count/len(list(adjacency_list.keys()))+0.001,2))