from collections import deque

N = int(input())
K = int(input())
queue = deque(range(1, N+1))
result = []
j = 1
while queue:
    if j % K == 0:
        result.append(queue.popleft())
    else:
        queue.append(queue.popleft())
    j += 1

print(f"<{', '.join(map(str, result))}>")