"""https://open.kattis.com/problems/backspace"""
bjarki = []
for c in input():
    bjarki.append(c) if c.isalpha() else bjarki.pop()
print(''.join(bjarki))