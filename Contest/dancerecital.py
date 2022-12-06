n = int(input())
lines = [input() for _ in range(n)]
quick_swaps = set()

def permutations(list):
    list_of_lists= list()
    for i in range(len(list)):
        
    return list_of_lists#list of lists [[abc,def],[def,abc]]

for i in range(1): #CHANGE
    # Rearrange for new order (factorial)
    newLines = lines.copy()
    
    # Get quick swaps
    for j in range(n - 1):
        quick_swap = 0
        stack = set()
        r1 = newLines[j]
        r2 = newLines[j + 1]
        for c in r1:
            stack.add(c)
        for c in r2:
            if c in stack:
                quick_swap += 1
        quick_swaps.add(quick_swap)
print(min(quick_swaps))
