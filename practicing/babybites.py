"""https://open.kattis.com/problems/babybites"""
nBites = int(input())
babyWords = list(input().split())
conclu = "makes sense"
for i in (range(nBites)):
    if babyWords[i] == "mumble" or babyWords[i] == str(i + 1):
        continue
    else:
        conclu = "something is fishy"
        break
print(conclu)