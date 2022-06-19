import sys

str_1 = list(input())
str_2 = []

for i in range(int(input())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L' and str_1:
        str_2.append(str_1.pop())

    elif command[0] == 'D' and str_2:
        str_1.append(str_2.pop())

    elif command[0] == 'B' and str_1:
        str_1.pop()

    elif command[0] == 'P':
        str_1.append(command[1])

print("".join(str_1 + list(reversed(str_2))))
