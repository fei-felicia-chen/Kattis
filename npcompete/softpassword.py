s = input()
p = input()

if s.lower() == p.lower():
    print("Yes")
elif s[0].isdigit() and s[1:] == p:
    print("Yes")
elif s[-1].isdigit() and s[:-1] == p:
    print("Yes")
else:
    print("No")