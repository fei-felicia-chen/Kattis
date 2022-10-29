"""https://open.kattis.com/problems/register"""
mylist = [1, 2, 6, 30, 210, 2310, 30030, 510510]
m = [1, 2, 4, 6, 10, 12, 16, 18]
inp = list(map(int, input().split()))
f = 0
for i in range(8):
    f += (m[i] - inp[i]) * mylist[i]
print(f)