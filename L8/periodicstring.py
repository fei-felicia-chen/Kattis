s = input()

def periodic(k):
    if len(s) % k != 0:
        return False
    curr = s[:k]
    s_copy = s[:]
    while s_copy:
        if not s_copy.startswith(curr):
            return False
        s_copy = s_copy[k:]
        curr = curr[-1] + curr[:-1]
    return True

for k in range(1, len(s) + 1):
    if periodic(k):
        print(k)
        break