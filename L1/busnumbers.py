numOfBuses = int(input())
busNumbers = list(map(int, input().split()))
busNumbers.sort()
shortRep = list()

i = 0
while True:
    if i >= numOfBuses:
        break
    myBus = busNumbers[i]
    if str(myBus) not in ' '.join(shortRep):
        shortRep.append(str(myBus)) 
    
    if i + 1 >= numOfBuses:
        break
    
    if busNumbers[i + 1] - myBus != 1:                                          # non consecutive
        i += 1
    elif i + 2 < numOfBuses and busNumbers[i + 2] - busNumbers[i + 1] != 1:     # second and third after are not consecutive
        shortRep.append(str(busNumbers[i + 1]))
        i += 2
    elif i + 2 >= numOfBuses:
        shortRep.append(str(busNumbers[i + 1]))
        i += 2
    else:
        while busNumbers[i + 1] - busNumbers[i] == 1 and i < numOfBuses:        # at least 3 consecutives
            shortRep[-1] = str(myBus) + ('-') + str(busNumbers[i + 1])
            i += 1
            if i + 1 == numOfBuses:
                break

print(' '.join(shortRep))