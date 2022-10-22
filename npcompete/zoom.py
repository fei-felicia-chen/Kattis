n, k = map(int, input().split())
numList = list(map(int, input().split()))
i = k-1
toReturn = ""
while i < n:
    toReturn += str(numList[i]) + " "
    i += k
print(toReturn)