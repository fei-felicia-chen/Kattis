#doesn't work
n, m = map(int, input().split())
receivers = set()
givers = set()
for _ in range(m):
    a, b = map(int, input().split())
    receivers.add(a)
    givers.add(b)
print("NO" if receivers != givers else "YES")