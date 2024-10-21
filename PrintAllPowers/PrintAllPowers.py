adjacency_list = {}
allPowerIns = []
allPowerOuts = []
length = 0
iteration = 1
iteration2 = 0
PowerIn = 0
PowerOut = 0
while True:
    try:
        temp_list = list(map(str,input().split()))
    except EOFError:
        break
    if temp_list == []:
        break
    adjacency_list.update({temp_list[0]: temp_list[1:]})
    length +=1
while iteration <= length:
    iteration2 = 1
    PowerIn = 0
    PowerOut = len(adjacency_list[str(iteration)])
    while iteration2 <= length:
        if str(iteration) in adjacency_list[str(iteration2)]:
            PowerIn += 1
        iteration2 += 1
    allPowerIns.append(str(PowerIn))
    allPowerOuts.append(str(PowerOut))
    iteration += 1
print("Stopnie wejściowe: "+ ' '.join(allPowerIns))
print("Stopnie wyjściowe: "+ ' '.join(allPowerOuts))
