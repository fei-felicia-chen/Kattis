def area(xa, ya, xb, yb, xc, yc):
    return abs((xa*(yb-yc) + xb*(yc-ya)+ xc*(ya-yb)) / 2.0)

xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
num_trees = int(input())
land1 = area(xa,ya,xb,yb,xc,yc)
print(round(land1, 1))

ante = 0
for _ in range(num_trees):
    ax, ay = map(int, input().split())
    land2 = area(xa,ya,ax,ay,xc,yc) + area(ax,ay,xb,yb,xc,yc) + area(xa,ya,xb,yb,ax,ay)
    if land2 == land1:
        ante += 1  
print(ante)
