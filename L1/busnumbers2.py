"""https://open.kattis.com/problems/busnumbers"""
numOfBuses = int(input())
busList = sorted(map(int, input().split()))

shortList = []

i = 0
while i < numOfBuses:
    j = 0
    while True:
        if i + j + 1 >= numOfBuses:
            break
        if busList[i + j + 1] - busList[i + j] != 1:
            break
        j += 1                      # j is the number of consecutives we have
    
    if j < 2:
        shortList.append(str(busList[i]))
        i += 1
    else:
        shortList.append(str(busList[i]) + "-" + str(busList[i + j]))
        i += j + 1

print(' '.join(shortList))