"""dumb way to do babybites, idk why i did this"""
nBites = int(input())
biteCounts = list()
for bite in (list(input().split())):
    try:
        biteCounts.append(int(bite))
    except:  
        biteCounts.append(1) if not biteCounts else biteCounts.append(biteCounts[-1] + 1)

if biteCounts != list(range(1, nBites + 1)):
    print("something is fishy")
else:
    print("makes sense")
    
