n = int(input())
plates = [int(input()) for _ in range(n)]
minV = min(plates)
M = []
for i in range(2, minV + 1):
    b = True
    modulo = plates[0] % i
    for j in range(1, n):
        if plates[j] % i != modulo:
            b = False
            break
    if b:
        M.append(i)
print(' '.join(map(str, M)))
