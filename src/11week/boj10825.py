n = int(input())
score = list(list())
for i in range(n):
    score.append(input().split())
    score[i][1] = int(score[i][1])
    score[i][2] = int(score[i][2])
    score[i][3] = int(score[i][3])

score.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(score[i][0])