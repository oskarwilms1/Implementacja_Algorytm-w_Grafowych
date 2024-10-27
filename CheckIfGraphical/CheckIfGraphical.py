user_input = input().split(' ')
iteration = 0
is_graphical = "TAK"
while iteration < len(user_input):
    user_input[iteration]= int(user_input[iteration])
    iteration +=1
iteration = 0
length = len(user_input)
while iteration < length: 
    user_input.sort(reverse = True)
    iteration2 = 0
    temp = int(user_input[iteration2])
    user_input.pop(0)
    while iteration2 <= temp-1:
        user_input[iteration2] = user_input[iteration2] - 1
        iteration2 +=1
    if -1 in user_input:
        is_graphical = "NIE"
        break
    iteration +=1
print(is_graphical)