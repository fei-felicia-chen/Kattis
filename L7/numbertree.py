inp = input().split()
if len(inp) == 1:
    height = inp.pop()
    description = ""
else:
    description = inp.pop()
    height = inp.pop()

height = int(height)
curr = 1

for c in description:
    curr <<= 1
    if c == 'R':
        curr += 1
        
print(2**(height + 1) - curr)
