user_input = input().split(' ')
iteration = 0
is_graphical = "TAK"
while iteration < len(user_input):
    user_input[iteration]= int(user_input[iteration])
    iteration +=1
iteration = 0
while iteration < len(user_input): 
    user_input.sort(reverse = True)
    iteration2 = iteration
    temp = int(user_input[iteration])
    user_input.pop(0)
    if iteration == temp:
        user_input[0] = user_input[0] - 1
    while iteration2 < temp:
        user_input[iteration2] = user_input[iteration2] - 1
        iteration2 +=1
    if -1 in user_input:
        is_graphical = "NIE"
    iteration +=1
print(is_graphical)