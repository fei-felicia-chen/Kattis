"""https://open.kattis.com/problems/closestsums"""
def findClosest(numList, sum):
    closest = numList[0] + numList[1]
    for i in range(len(numList) - 1):
        for j in range(i + 1, len(numList)):
            cur = numList[i] + numList[j]
            if cur == sum:
                return cur
            if abs(sum - cur) < abs(sum - closest):
                closest = cur
    return closest

case = 1

while True:
    # get input
    try:
        size = int(input())
    except:
        break
    numList = []
    for i in range(size):
        numList.append(int(input()))
    sumList = []
    for i in range(int(input())):           # num of sums as input
        sumList.append(int(input()))
    
    print("Case " + str(case) + ":")
    for i in range(len(sumList)):
        print("Closest sum to " + str(sumList[i]) + " is",
              str(findClosest(numList, sumList[i])) + ".")
    case += 1