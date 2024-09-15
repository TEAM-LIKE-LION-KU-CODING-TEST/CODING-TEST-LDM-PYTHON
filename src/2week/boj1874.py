import sys

N = int(input())
array = [sys.stdin.readline().strip() for i in range(N)]
num = list(map(int, array))
stack = []
save = []
check = []
end_v = num[0]
start_v = 1

for i in range(N):
    end_v = num[i]
    if start_v <= end_v:
        for j in range(start_v, end_v + 1):
            stack.append(j)
            save.append("+")

            if stack and stack[-1] == num[i]:
                pop = stack.pop()
                save.append("-")
    else:
        if stack and stack[-1] == num[i]:
            pop = stack.pop()
            save.append("-")
        else:
            check.append("NO")
    if start_v <= end_v + 1:
        start_v = end_v + 1
if check:
    print(check[0])
else:
    for a in save:
        print(a)