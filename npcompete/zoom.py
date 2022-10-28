n, k = map(int, input().split())
numList = list(map(int, input().split()))
i = k-1
while i < n:
    print(numList[i], end=' ', flush=False)
    i += k