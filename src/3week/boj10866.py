import sys
from collections import deque

N = int(input())
str = [sys.stdin.readline().strip() for i in range(N)]
deque = deque()
for i in range(0,N):
    if "push_front" in str[i]:
        deque.appendleft(str[i].strip("push_front").strip())
    elif "push_back" in str[i]:
        deque.append(str[i].strip("push_back").strip())
    elif "pop_front" in str[i]:
        if len(deque)==0:
            print("-1")
        else:
            print(deque.popleft())
    elif "pop_back" in str[i]:
        if len(deque)==0:
            print("-1")
        else:
            print(deque.pop())
    elif "size" in str[i]:
        print(len(deque))
    elif "empty" in str[i]:
        if len(deque)==0:
            print("1")
        else:
            print("0")
    elif "front" in str[i]:
        if len(deque)==0:
            print("-1")
        else:
            print(deque[0])
    elif "back" in str[i]:
        if len(deque)==0:
            print("-1")
        else:
            print(deque[-1])