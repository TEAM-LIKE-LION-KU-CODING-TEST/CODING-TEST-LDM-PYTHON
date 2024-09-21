from collections import deque

N, M = map(int, input().split())
num = list(map(int, input().split()))
dq = deque([i for i in range(1, N+1)])
c = 0
for n in num:
    while True:
        if n == dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(n) > len(dq)//2:
                dq.rotate(1)
                c += 1
            else:
                dq.rotate(-1)
                c += 1
print(c)