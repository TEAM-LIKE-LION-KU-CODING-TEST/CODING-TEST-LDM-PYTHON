import sys
from collections import deque


def bfs(x):
    dp = deque([x])
    while dp:
        x = dp.popleft()
        if x == k:
            return array[x]
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < 100001 and not array[i]:
                array[i] = array[x] + 1
                dp.append(i)


n, k = map(int, sys.stdin.readline().split())
array = [0] * 100001
print(bfs(n))
