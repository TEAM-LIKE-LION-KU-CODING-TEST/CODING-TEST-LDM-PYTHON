import sys

word1 = list(sys.stdin.readline().strip())
word2 = list(sys.stdin.readline().strip())
cnt = 0

for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            word1.pop(i)
            word1.insert(i,0)
            word2.pop(j)
            word2.insert(j,0)

for i in range(len(word1)):
    if word1[i] != 0:
        cnt += 1

for j in range(len(word2)):
    if word2[j] != 0:
        cnt += 1

print(cnt)