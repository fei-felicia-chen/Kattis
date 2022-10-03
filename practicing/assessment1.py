def funcAlphabeticOrder(inputSting):
    sortedString = ''.join(sorted(inputSting))
    if sortedString == inputSting: return 0
    else:
        for index, char in enumerate(inputSting):
            if char != sortedString[index]: return index + 1
def main():
	#input for inputSting
	inputSting = str(input()).lower()
 
 
	result = funcAlphabeticOrder(inputSting)
	print(result)

if __name__ == "__main__":
	main()