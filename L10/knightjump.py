from collections import deque

jump_dir = {(-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (2, 1), (2, -1), (-1, -2)}
n = int(input())
x, y = -1, -1
arr = []
for i in range(n):
    row = input()
    arr.append(row)
    for j in range(n):
        if row[j] == 'K':
            x, y = i, j
visited = [[False for __ in range(n)] for _ in range(n)]

def valid_pos(x, y):
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= n:
        return False
    if arr[x][y] == '#':
        return False
    if visited[x][y]:
        return False
    return True

        
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
            visited[r+x][c+y] = True
            
print(-1)
