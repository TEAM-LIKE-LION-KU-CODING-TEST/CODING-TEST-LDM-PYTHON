from collections import deque

n, k = map(int, input().split())
max = 100001
distance = [0] * max
visited = [False] * max

dp = deque()
dp.append(n)
visited[n] = True

def BFS(k):
    while dp:
        x = dp.popleft()
        if x == k:
            return distance[k]
        if 0 <= 2 * x < max and not visited[2 * x]:
            t = 2 * x
            distance[t] = distance[x]
            visited[t] = True
            dp.append(t)

        if 0 <= x - 1 < max and not visited[x - 1]:
            t = x - 1
            distance[t] = distance[x] + 1
            visited[t] = True
            dp.append(t)

        if 0 <= (x + 1) < max and not visited[x + 1]:
            t = x + 1
            distance[t] = distance[x] + 1
            visited[t] = True
            dp.append(t)

print(BFS(k))