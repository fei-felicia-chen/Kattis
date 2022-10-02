
"""
matrix, represents the elements of the matrix of size N*M.
"""
def funcMatrix(matrix):
	# Write your code here
    mySet = set()
    for i in range(len(matrix)):
        myMax = 0
        for j in range(len(matrix[i])):
            myMax = max(myMax, matrix[i][j])
        mySet.add(myMax)                    # max of a row
    for j in range(len(matrix[0])):
        myMin = 2000
        for i in range(len(matrix)):
            myMin = min(myMin, matrix[i][j])
        if myMin in mySet:
            return myMin
    return -1

def main():
	#input for matrix
	matrix = []
	matrix_rows,_  = map(int, input().split())
	for _ in range(matrix_rows):
		matrix.append(list(map(int, input().split())))
	result = funcMatrix(matrix)
	print(result)

if __name__ == "__main__":
	main()