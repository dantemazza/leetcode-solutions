class Node:
    val = 0
    currMin = 0
    next = None

    def __init__(self, val, currMin):
        self.val = val
        self.currMin = currMin

class MinStack:
    head = None
    currMin = sys.maxsize

    def __init__(self):
        x = 9
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        if x < self.currMin:
            self.currMin = x
        node = Node(x, self.currMin)
        if self.head:
            node.next = self.head
        self.head = node

    def pop(self) -> None:
        if not self.head:
            return
        else:
            self.head = self.head.next
            if self.head:
                self.currMin = self.head.currMin
            else:
                self.currMin = sys.maxsize

    def top(self) -> int:
        if self.head:
            return self.head.val
        else:
            return None

    def getMin(self) -> int:
        return self.currMin

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
