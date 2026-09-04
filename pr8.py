# Linked List Implementation
# Singly, Doubly and Circular Linked List


# ---------------- SINGLY LINKED LIST ----------------

class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = SinglyNode(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


print("SINGLY LINKED LIST")
sll = SinglyLinkedList()

sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.insert(40)

print("List:")
sll.display()


# ---------------- DOUBLY LINKED LIST ----------------

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


print("\nDOUBLY LINKED LIST")
dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

print("List:")
dll.display()


# ---------------- CIRCULAR LINKED LIST ----------------

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = CircularNode(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if self.head is None:
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


print("\nCIRCULAR LINKED LIST")
cll = CircularLinkedList()

cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

print("List:")
cll.display()