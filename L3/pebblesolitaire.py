def checkNextMoves(line, q):
    for i in range(10):
        jumpable = line[i:i+3]
        if jumpable == ['o', 'o', '-']:
            q.append(line[:])
            q[-1][i:i+3] = ['-', '-', 'o']
        elif jumpable == ['-', 'o', 'o']:
            q.append(line[:])
            q[-1][i:i+3] = ['o', '-', '-']

for game in range(int(input())):
    q = []
    line = list(input())
    checkNextMoves(line, q)
    if not q:
        print(line.count('o'))
    else:
        score = 12
        while q:
            line = q.pop()
            if score > line.count('o'):
                score = line.count('o')
            checkNextMoves(line, q)
        print(score)