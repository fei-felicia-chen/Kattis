"""https://open.kattis.com/problems/doorman"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def get(self):
        return self.data
    
    def __str__(self):
        return "(" + str(self.data) + ")"

class ClubLine:
    def __init__(self, head):
        self.head = head
        self.last = head
        
    def __init__(self):
        self.head = None
        self.last = None
    
    def isEmpty(self):
        return self.head is None

    def addLast(self, last):
        node = Node(last)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            tmp = self.last
            self.last = node
            self.last.last = None
            self.last.prev = tmp

    def removeFirst(self):
        if self.head.next is None: # only 1 node
            self.head = None
            self.last = None
        else:
            if self.head.next.next is None: # only 2 nodes
                self.last = self.head.next
            self.head.next.prev = None
            self.head = self.head.next
            
    def hasSecond(self):
        if self.head is None:
            return False
        if self.head.next is None:
            return False
        return True
        
    def removeSecond(self):
        first = self.head
        if first.next.next is not None:
            third = first.next.next
            first.next = third
            third.prev = first
        else:
            first.next = None
            self.last = first

    def __str__(self):
        if self.head is None:
            return "()"
        to_return = str(self.head)
        cur = self.head
        while cur.next is not None:
            to_return += " -> " + str(cur.next)
            cur = cur.next
        return to_return
            
if __name__ == "__main__":
    iq = int(input())
    q = input()
    line = ClubLine()
    for human in range(len(q)):
        line.addLast(q[human])
    diff = 0
    entered = 0                      # total humans entered in the club
    while abs(diff) <= iq:
        if line.isEmpty():
            break
        
        if abs(diff) < iq:
            if line.head.get() == "W":
                diff -= 1
            if line.head.get() == "M":
                diff += 1
            entered += 1
            line.removeFirst()
            
        elif abs(diff) == iq:
            if diff > 0:
                if line.head.get() == "W":
                    diff -= 1
                    entered += 1
                    line.removeFirst()
                elif line.head.next.get() == "W":
                    diff -= 1
                    entered += 1
                    line.removeSecond()
                else:
                    break
            elif diff < 0:
                if line.head.get() == "M":
                    diff += 1
                    entered += 1
                    line.removeFirst()
                elif line.head.next.get() == "M":
                    diff += 1
                    entered += 1
                    line.removeSecond()
                else:
                    break
        else:
            break
    print(entered)