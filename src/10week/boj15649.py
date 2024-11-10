import itertools

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
array = itertools.permutations(num, m)
for i in array:
    for j in i:
        print(j, end = ' ')
    print()
