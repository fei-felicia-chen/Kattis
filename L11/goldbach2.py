primes = []
for i in range(2, 32000):
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            break
    else:
        primes.append(i)

for _ in range(int(input())):
    setp = set(primes)
    reps = []
    n = int(input())
    for p in primes:
        if p < n and (n-p) in setp:
            setp.remove(p)
            reps.append((p, (n-p)))
    print(f"{n} has {len(reps)} representation(s)")
    for a, b in reps:
        print(f"{a}+{b}")