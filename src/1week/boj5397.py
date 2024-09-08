import sys

T = int(input())
for _ in range(T):
    L = sys.stdin.readline().strip()
    left = []
    right = []

    for c in L:
        if c == '-':
            if left:
                left.pop()
        elif c == '<':
            if left:
                right.append(left.pop())
        elif c == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(c)
    print(''.join(left + right[::-1]))