cases = int(input())
for case in range(cases):
    input()
    lst = list(map(int, input().split()))
    count = {}
    for p in lst:
        if p in count:
            del count[p]
        else:
            count[p] = 1
    a, _= count.popitem()
    print("Case #" + str(case + 1) + ": " + str(a))
