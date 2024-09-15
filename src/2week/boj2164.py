from collections import deque
N = int(input())
queue = deque(range(1, N + 1))
j = 0

while len(queue) != 1:
    if j % 2 == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    j += 1

print(queue[0])
