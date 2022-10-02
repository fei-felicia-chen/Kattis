"""https://open.kattis.com/problems/plantingtrees"""
input()
trees = sorted(list(map(int, (input().split()))), reverse=True)
earliest = 0
for day, tree in enumerate(trees):
    if day + tree > earliest:
        earliest = day + tree
print(earliest + 2)