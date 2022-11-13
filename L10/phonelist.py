t = int(input())
for _ in range(t):
    num = []
    n = int(input())
    for _ in range(n):
        num.append(input())
    num.sort()
    result = "YES"
    for i in range(n-1):
        if len(num[i]) <= len(num[i + 1]):
            if num[i] == num[i+1][:len(num[i])]:
                result = "NO"
                break
    print(result)
    