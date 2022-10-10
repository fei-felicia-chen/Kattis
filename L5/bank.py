"""https://open.kattis.com/problems/bank"""
# This program gives and index out of range at a specific edge case, not sure why
# See the Golang and/or Java versions.
N, T = map(int, input().split())
q = [0 for _ in range(N)]                           # initialize queue of size N
for _ in range(N):
    cash, time = map(int, input().split())
    if q[time] == 0:                                # if no one in that queue spot
        q[time] = cash
    else:
        for minute in range(time, -1, -1):          # check for every min of the wait time 
            if q[minute] < cash:                    # if there is anyone depositing less money
                q[minute], cash = cash, q[minute]   # swap and check again
print(sum(q))
