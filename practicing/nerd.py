ct = 1
while True:
    try:
        l = list(map(int, input().split()))
        l = l[1:]
        maximum = max(l)
        minimum = min(l)
        print("Case {c}: {min} {max} {range}".format(
            c=ct, min=minimum, max=minimum, range=maximum - minimum))
        ct += 1
    except:
        break