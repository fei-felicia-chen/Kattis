case = 0
while True:
    case += 1
    try:
        inp = list(map(int, input().split()))
        inp = inp[1:]
    except:
        break
    print("Case " + str(case) + ": " + str(min(inp)) + " " + str(max(inp)) + " " + str(max(inp) - min(inp)))