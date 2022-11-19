class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return "(" + str(self.data) + ")"

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.last = head
    
    def __init__(self):
        self.head = None
        self.last = None

    def addLast(self, last):
        node = Node(last)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
            self.last.next = None

    def get(self, index):
        curr = self.head
        while index != 0:
            if curr is None:
                raise ValueError
            curr = curr.next
            index -= 1
        return curr

    def remove(self, index):
        if index == 0:
            if self.head is None:
                raise ValueError
            else:
                self.head = self.head.next
        else:
            prev = self.get(index-1)
            toRemove = prev.next
            tmp1 = toRemove.next
            prev.next = tmp1

lst = LinkedList()
lst.addLast("b")
lst.addLast("c")
lst.addLast("d")
print(lst.get(2))