import sys
sys.setrecursionlimit(10**7)
max = 60
T = int(input())

moveY = [1,-1,0,0]
moveX = [0,0,1,-1]
def dfs(y,x):
    global visited
    visited[y][x] = True
    for move_index in range(4):
        newY = y+moveY[move_index]
        newX = x+moveX[move_index]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY,newX)

for _ in range(T):
    M,N,K = map(int, input().split())
    graph = [[False] * max for _ in range(max)]
    visited = [[False] * max for _ in range(max)]

    for _ in range(K):
        x,y = map(int, input().split())
        graph[y+1][x+1] = True

    cnt = 0
    for i in range(1, N+1):
        for j in range(1,M+1):
            if graph[i][j] and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)
