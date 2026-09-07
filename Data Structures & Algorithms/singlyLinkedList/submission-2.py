class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def remove(self, index: int) -> bool:
        if index < 0 or not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1

        if not curr or not curr.next:
            return False

        curr.next = curr.next.next
        return True

    def getValues(self) -> list:
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result