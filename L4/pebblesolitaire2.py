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
    games[line] = line.count('o')
    play(list(line))
    while q:
        line = q.pop()
        lineString = ''.join(line)
        if lineString in games:
            continue
        games[lineString] = line.count('o')
        play(line)
    
    score_min = min(games.keys(), key=(lambda k: games[k]))        
    print(games[score_min])