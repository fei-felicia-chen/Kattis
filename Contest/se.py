class Coor:
    def __init__(self, x, y):
            self.x = x
            self.y = y
    
def distance(p1,p2):
    return math.sqrt(math.pow(p1.x-p2.x,2)+math.pow(p1.y-p2.y,2))
#used for DETERMINING SIGNED AREA OF TRIANGLE, COLINEARITY OF 3 POINTS, ORIENTATION OF 3 POINTS, TESTING INTERSECTION OF TWO LINE SEGMENTS
def ccw(a,b,c):
    return (b.x-a.x)(c.y-a.y)- (b.y-a.y)(c.x-a.x)
    
def is_left_turn(result_of_ccw):
    return result_of_ccw>0

def main():
    while True:
        try:
            n= int(input())
            l= list()
            distances
            for i in range(n):
                x,y= map(int, input().split())
                l.append(Coor(x,y))
            
            for i in range(len(l)-1):
                coor = l[i]
                coor2= l[i+1]
                distance= distance(coor,coor2)
                
            
            counterclockwise= is_left_turn(ccw(l[0],l[1],l[2]))
            
            
                 
        except:
            break
    