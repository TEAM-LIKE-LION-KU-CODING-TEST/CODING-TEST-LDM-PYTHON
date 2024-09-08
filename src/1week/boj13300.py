import sys

male = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0}
female = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0}
male_room = 0
female_room = 0

N, K = sys.stdin.readline().split(" ")
K = int(K)
for i in range(int(N)):
    S, Y = sys.stdin.readline().split(" ")
    if S == "0":
        female[Y.strip()]+=1
    else:
        male[Y.strip()]+=1

for i in range(1,7):
    male_room += male[str(i)]//K
    if male[str(i)] % K:
        male_room+=1
    female_room += female[str(i)] // K
    if female[str(i)] % K:
        female_room += 1

print(male_room+female_room)
