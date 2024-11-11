n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

minus_count = 0
zero_count = 0
one_count = 0


def check_same(x, y, n):
    first_value = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != first_value:
                return False
    return True


def count_paper(x, y, n):
    global minus_count, zero_count, one_count

    if check_same(x, y, n):
        if paper[x][y] == -1:
            minus_count += 1
        elif paper[x][y] == 0:
            zero_count += 1
        elif paper[x][y] == 1:
            one_count += 1
        return

    size = n // 3
    for i in range(3):
        for j in range(3):
            count_paper(x + i * size, y + j * size, size)


count_paper(0, 0, n)
print(minus_count)
print(zero_count)
print(one_count)


