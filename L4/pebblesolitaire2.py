"""https://open.kattis.com/problems/pebblesolitaire2"""
q = list()
games = dict()

def play(line):
    for i in range(21):
        jumpable = line[i:i+3]
        if jumpable == ['o', 'o', '-']:
            q.append(line[:])
            q[-1][i:i+3] = ['-', '-', 'o']
        elif jumpable == ['-', 'o', 'o']:
            q.append(line[:])
            q[-1][i:i+3] = ['o', '-', '-']

for game in range(int(input())):
    q.clear()
    games.clear()
    line = input()
    score = line.count('o')
    games[line] = 1
    play(list(line))
    while q:
        line = q.pop()
        if (lineString := ''.join(line)) in games:
            continue
        lineScore = line.count('o')
        if lineScore < score:
            score = lineScore
        games[lineString] = 1
        play(line)
   
    print(score)