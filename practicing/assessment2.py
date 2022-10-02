
"""
inputArr, represents the given array of element of size inputArr_size.
"""
def funcTwins(inputArr, inputSize):
	# Write your code here
    if inputSize == 1:
        return inputArr[0]
    myDict = {}
    nontwin = 100000
    for person in inputArr:
        if person not in myDict:
            myDict[person] = 1
        else:
            myDict[person] += 1
    for person in myDict:
        if myDict[person] == 1 and person < nontwin:
            nontwin = person
    return nontwin if nontwin != 100000 else -1

def main():
	#input for inputArr
	inputArr = []
	inputSize = int(input())
	inputArr = list(map(int,input().split()))
	
	
	result = funcTwins(inputArr, inputSize)
	print(result)	

if __name__ == "__main__":
	main()