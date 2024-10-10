"""Napisz program, który wczyta wiersz dowolnej długości, a następnie wypisze go w odwrotnej kolejności."""

user_string = list(map(str,input().split()))
final_string = []
for element in user_string:
    final_string.append("0")
i = -1
for element in user_string:
    final_string[i] = element
    i -=1
print(' '.join(final_string))
