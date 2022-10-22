a, b, c, d = map(float, input().split())
toreturn = abs(a - c)*abs(b - d)
print("{:.3f}".format(toreturn))