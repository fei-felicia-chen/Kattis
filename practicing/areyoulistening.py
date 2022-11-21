cx, cy, n = map(int, input().split())
radius = []

for i in range(n):
    x, y, r = map(int, input().split())
    d = ((cx - x)**2 + (cy - y)**2)**0.5 - r
    radius.append(int(d))

radius.sort()
ans = radius[2]
print(ans if ans > 0 else 0)
