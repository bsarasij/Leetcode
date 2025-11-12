class Node: 
    def __init__(self, x = None):
        self.val = x
        self.prev = None
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index + 1 < self.size - index:
            curr = self.head
            for i in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(self.size - index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        pred, succ = self.head, self.head.next
        self.size += 1
        to_add = Node(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add        

    def addAtTail(self, val: int) -> None:
        pred, succ = self.tail.prev, self.tail
        self.size += 1
        node = Node(val)
        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index < self.size - index:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for i in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        self.size += 1

        node = Node(val)
        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for i in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        
        pred.next = succ
        succ.prev = pred
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)