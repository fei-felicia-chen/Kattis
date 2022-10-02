"""https://open.kattis.com/problems/erase"""
n = int(input())
before = input()
after = input()
correct = True

if n % 2 == 0:
    if before != after:
        correct = False
else:
    for x, y in zip(before, after):
        if x == y:
            correct = False
            break

if correct:
    print("Deletion succeeded")
else:
    print("Deletion failed")