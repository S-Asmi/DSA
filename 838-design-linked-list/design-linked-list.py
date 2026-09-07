class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def getNode(self, index):
        if index < 0 or index >= self.length:
            return None

        counter = 0
        current = self.head

        while counter != index:
            counter += 1
            current = current.next

        return current


    def get(self, index):
        if index < 0 or index >= self.length:
            return -1

        counter = 0
        current = self.head

        while counter != index:
            counter += 1
            current = current.next

        return current.value


    def addAtHead(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            self.head = newNode
            newNode.next = temp
            temp.prev = newNode

        self.length += 1


    def addAtTail(self, val):
        newNode = Node(val)

        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next

        self.length += 1


    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return

        if index == 0:
            self.addAtHead(val)

        elif index == self.length:
            self.addAtTail(val)

        else:
            NodeAtCurrentIndex = self.getNode(index)
            newNode = Node(val)

            prevNodeFromCurrentIndex = NodeAtCurrentIndex.prev

            prevNodeFromCurrentIndex.next = newNode
            newNode.prev = prevNodeFromCurrentIndex

            newNode.next = NodeAtCurrentIndex
            NodeAtCurrentIndex.prev = newNode

            self.length += 1


    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            PrevNodeFromDelete = self.getNode(index - 1)
            NextNodeFromDelete = PrevNodeFromDelete.next.next

            PrevNodeFromDelete.next = NextNodeFromDelete
            NextNodeFromDelete.prev = PrevNodeFromDelete

        self.length -= 1