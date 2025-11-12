class Node:
    def __init__(self, key: int|None = None, value: int | None = None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodeMap: dict[int, Node] = {}

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        node = self.nodeMap[key]
        self.deleteNode(node)
        self.addAfterHead(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.deleteNode(node)
            self.addAfterHead(node)
        else:
            if len(self.nodeMap) == self.capacity:
                LRUNode = self.tail.prev
                self.deleteNode(LRUNode)
                self.nodeMap.pop(LRUNode.key)
            node = Node(key, value)
            self.nodeMap[key] = node
            self.addAfterHead(node)
            
    def deleteNode(self, node: Node) -> None:
        pred, succ = node.prev, node.next
        if pred is None or succ is Node:
            return
        pred.next = succ
        succ.prev = pred
    
    def addAfterHead(self, node: Node) -> None:
        pred, succ = self.head, self.head.next
        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)