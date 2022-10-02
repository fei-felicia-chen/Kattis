"""https://open.kattis.com/problems/commercials"""
n, cost = map(int, input().split())
revenues = map(int, input().split())
profits = [revenue - cost for revenue in revenues]

for i in range(1, n):
    curr = profits[i - 1] + profits[i]
    if curr > profits[i]: profits[i] = curr
print(max(profits))