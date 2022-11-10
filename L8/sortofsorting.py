from functools import cmp_to_key

def compare(a, b):
    """Compare first characters"""
    if a[0] > b[0]:
        return 1
    if a[0] < b[0]:
        return -1
    """Compare second characters since first would have to be equal"""
    if a[1] > b[1]:
        return 1
    if a[1] < b[1]:
        return -1
    return 0                            # error

while ((n := int(input())) != 0):
    names = [input() for _ in range(n)]
    names.sort(key=cmp_to_key(compare))
    for name in names:
        print(name)
    print()                             # print newline