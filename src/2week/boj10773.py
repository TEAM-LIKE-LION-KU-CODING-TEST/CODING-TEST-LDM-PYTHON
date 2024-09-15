stack = []
K = int(input())
for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        if stack:
            stack.pop()

sum_ = sum(stack)
print(sum_)
