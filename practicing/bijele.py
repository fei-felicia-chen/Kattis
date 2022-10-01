default = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
missing = []
for n, m in zip(default, found):
    missing.append(n - m)
print(' '.join(map(str, missing)))