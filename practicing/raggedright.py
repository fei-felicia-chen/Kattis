"""https://open.kattis.com/problems/raggedright"""
lengths = []
score = 0
while True:
    try:
        lengths.append(len(input()))
    except:
        break

longest = max(lengths)
lengths = lengths[:-1]
for length in lengths:
    if length == longest:
        continue
    else:
        score += (longest - length) ** 2
            
print(score)