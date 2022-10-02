"""https://open.kattis.com/problems/countingstars"""
def hasTop(matrix, i, j):
    if (i - 1 < 0):                                    # check for border
        return False
    if (matrix[i - 1][j] == "-"):                      # check top
        return True
    return False

def hasBottom(matrix, i, j, m):
    if (i + 1 >= m):                                   # check for border      
        return False
    if (matrix[i + 1][j] == "-"):                      # check bottom
        return True
    return False

def hasRight(matrix, i, j, n):
    if (j + 1 >= n):                                   # check for border
        return False
    if matrix[i][j + 1] == "-":                        # check right
        return True
    return False

def hasLeft(matrix, i, j):
    if (j - 1 < 0):                                    # check for border
        return False
    if matrix[i][j - 1] == "-":                        # check left
        return True
    return False
    
def queueNeighbours(matrix, i, j, m, n, visited, queue):
    if hasTop(matrix, i, j) and not visited[i - 1][j]:          # queue top
        queue.append((i - 1, j))
    if hasRight(matrix, i, j, n) and not visited[i][j + 1]:     # queue right
        queue.append((i, j + 1))
    if hasBottom(matrix, i, j, m) and not visited[i + 1][j]:    # queue bottom
        queue.append((i + 1, j))
    if hasLeft(matrix, i, j) and not visited[i][j - 1]:         # queue left
        queue.append((i, j - 1))

caseCount = 1
while True:
    try:
        line = input()                                 # get row and col
    except:
        break
    
    if not line:                                       # check for empty input
        break
    starCount = 0
    m, n = [int(x) for x in line.split()]              # m = total row, col = pixel per row
    
    sky, queue = [], []                                
    [sky.append(list(input())) for i in range(m)]      # add rows to sky
    visited = [[False for j in range(n)] for i in range(m)]
    
    for i in range(m):                                 # for every row
        for j in range(n):                             # for every pixel
            if sky[i][j] == "-" and not visited[i][j]: # find star characters
                starCount += 1                         # found star character
                visited[i][j] = True                   # mark as visited
    #           sky[i][j] = starCount                  # change char to star count <---------- debug line
                queueNeighbours(sky, i, j, m, n, visited, queue)
                while queue:
                    row, col = queue.pop(0)
                    if not visited[row][col]:
                        visited[row][col] = True
    #                   sky[row][col] = starCount
                        queueNeighbours(sky, row, col, m, n, visited, queue)
                        
    print("Case " + str(caseCount) + ": " + str(starCount))
    # print(sky)                                         # <---------- debug line
    caseCount += 1