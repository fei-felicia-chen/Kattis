"""https://open.kattis.com/problems/bijele"""
default = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
missing = []
[missing.append(n - m) for n, m in zip(default, found)]
print(' '.join(map(str, missing)))