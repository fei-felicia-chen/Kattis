from collections import deque

jump_dir = {(-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (2, 1), (2, -1), (-1, -2)}
n = int(input())
arr = [[c for c in input()] for _ in range(n)]
visited = [[False for __ in range(n)] for _ in range(n)]

def valid_pos(x, y):
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= n:
        return False
    if arr[x][y] != '.':
        return False
    if visited[x][y]:
        return False
    return True
    

# Find knight
x, y = (-1, -1)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'K':
            x, y = i, j
            break
        
# Queue possible moves
q = deque()
q.append((x, y, 0))
while q:
    x, y, score = q.popleft()
    if x == 0 and y == 0:
        print(score)
        exit()
    for dir in jump_dir:
        r, c = dir
        if valid_pos(r + x, c + y):
            q.append((r+x, c+y, score+1))
            visited[x][y] = True
            
print(-1)
