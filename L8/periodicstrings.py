"""https://open.kattis.com/problems/periodicstrings"""
s = input()

def periodic(k):
    if len(s) % k != 0:
        return False
    curr = s[:k]
    i = 0
    while i < len(s):
        if not s[i:i+k] == curr:
            return False
        i += k
        curr = curr[-1] + curr[:-1]
    return True

for k in range(1, len(s) + 1):
    if periodic(k):
        print(k)
        break
