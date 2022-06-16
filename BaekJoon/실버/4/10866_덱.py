from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

for i in range(N):
    command = input().split()

    if command[0] == "push_front":
        # push_front
        q.appendleft(command[1])

    elif command[0] == "push_back":
        # push_back
        q.append(command[1])

    elif command[0] == "pop_front":
        # pop_front
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif command[0] == "pop_back":
        # pop_back
        if q:
            print(q.pop())
        else:
            print(-1)

    elif command[0] == "size":
        # size
        print(len(q))

    elif command[0] == "empty":
        # empty
        if q:
            print(0)
        else:
            print(1)

    elif command[0] == "front":
        # front
        if q:
            print(q[0])
        else:
            print(-1)

    elif command[0] == "back":
        # back
        if q:
            print(q[len(q) - 1])
        else:
            print(-1)