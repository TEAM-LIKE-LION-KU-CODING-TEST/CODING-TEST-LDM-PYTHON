import sys
from collections import deque
N = int(input())
str = [sys.stdin.readline().strip() for i in range(N)]
queue = deque()
for i in range(0,N):
    if "push" in str[i]:
        queue.append(str[i].strip("push").strip())
    elif "pop" in str[i]:
        if len(queue)==0:
            print("-1")
        else:
            print(queue.popleft())
    elif "size" in str[i]:
        print(len(queue))
    elif "empty" in str[i]:
        if len(queue)==0:
            print("1")
        else:
            print("0")
    elif "front" in str[i]:
        if len(queue)==0:
            print("-1")
        else:
            print(queue[0])
    elif "back" in str[i]:
        if len(queue)==0:
            print("-1")
        else:
            print(queue[-1])