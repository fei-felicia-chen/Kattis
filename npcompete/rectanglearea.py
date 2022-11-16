a, b, c, d = map(float, input().split())
ans = abs(a - c)*abs(b - d)
print("{:.3f}".format(ans))