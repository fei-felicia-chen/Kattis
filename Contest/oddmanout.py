cases = int(input())
for case in range(1, cases + 1):
    input()
    lst = list(map(int, input().split()))
    count = set()
    for p in lst:
        if p in count:
            count.remove(p)
        else:
            count.add(p)
    a = count.pop()
    print("Case #" + str(case) + ": " + str(a))
