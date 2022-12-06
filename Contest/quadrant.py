a = int(input())
b = int(input())
if a > 0 and b > 0:
    print("1")
    exit()
elif a > 0 and b < 0:
    print("4")
    exit()
elif a < 0 and b > 0:
    print("2")
    exit()
print("3")