class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = SinglyNode(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()


print("Singly linked list")
singly = SinglyLinkedList()
singly.insert(10)
singly.insert(20)
singly.insert(30)
print("After insertion:")
singly.traverse()
singly.delete(20)
print("After deleting 20:")
singly.traverse()


class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = DoublyNode(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.previous = current

    def delete(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                if current.previous is None:
                    self.head = current.next
                else:
                    current.previous.next = current.next

                if current.next is not None:
                    current.next.previous = current.previous
                return

            current = current.next

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()


print("Doubly linked list")
doubly = DoublyLinkedList()
doubly.insert(10)
doubly.insert(20)
doubly.insert(30)
print("After insertion:")
doubly.traverse()
doubly.delete(20)
print("After deleting 20:")
doubly.traverse()


class CircularNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = CircularNode(value)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        current = self.head
        while current.next is not self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def delete(self, value):
        if self.head is None:
            return

        current = self.head
        previous = None

        while True:
            if current.value == value:
                if previous is None:
                    if current.next is self.head:
                        self.head = None
                    else:
                        last = self.head
                        while last.next is not self.head:
                            last = last.next

                        self.head = current.next
                        last.next = self.head
                else:
                    previous.next = current.next
                return

            previous = current
            current = current.next

            if current is self.head:
                return

    def traverse(self):
        if self.head is None:
            print()
            return

        current = self.head
        while True:
            print(current.value, end=" ")
            current = current.next

            if current is self.head:
                break

        print()


print("Circular linked list")
circular = CircularLinkedList()
circular.insert(10)
circular.insert(20)
circular.insert(30)
print("After insertion:")
circular.traverse()
circular.delete(20)
print("After deleting 20:")
circular.traverse()

