class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            if temp is None:
                print("Linked List is Empty")
                return
            else:
                print(temp.data)
                temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def inserAtMiddle(self, prev_data, new_data):
        new_node = Node(new_data)
        temp = self.head
        prev = None
        while temp:
            if temp.data == prev_data:
                new_node.next = temp.next
                temp.next = new_node
                return
            else:
                prev = temp
                temp = temp.next

    def insertNodeAtPosition(self, new_data, position):

        new_node = Node(new_data)
        temp = self.head

        if position == 0:
            new_node.next = temp
            self.head = new_node

        else:
            count = 0
            prev_node = None
            while temp:
                if count == position:
                    prev_node.next = new_node
                    new_node.next = temp
                    return

                prev_node = temp
                temp = temp.next
                count += 1
            prev_node.next = new_node

            return

    def append(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        if self.head is None:
            self.head = new_node
        else:
            while temp:
                if temp.next is None:
                    temp.next = new_node
                    new_node.next = None
                    return
                else:
                    temp = temp.next

    def deleteNode(self, position):
        temp = self.head
        if position == 0:
            self.head = temp.next
            return

        else:
            count = 0
            prev_node = None
            while temp:
                if count == position:
                    prev_node.next = temp.next
                    return
                prev_node = temp
                temp = temp.next
                count += 1
            return

    def delMiddle(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        prev = None
        while temp:
            if temp.data == new_data:
                prev.next = temp.next
                return
            else:
                prev = temp
                temp = temp.next

    def reversePrint(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

        return

    def reverse(self):
        previous = None
        current = self.head
        following = current.next

        while current:
            current.next = previous
            previous = current
            current = following
            if following:
                following = following.next
        self.head = previous

    def printReverse(self, temp):
        if temp:
            self.printReverse(temp.next)
            print(temp.data)
        else:
            return


llist = Linkedlist()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
llist.printlist()
print()

print()
print("after push operation")
llist.push(0)
llist.printlist()

print()
print("after append operation")
llist.append(4)
llist.printlist()

print()
print("after isnertAtMiddle operation")
llist.inserAtMiddle(2, 2.1)
llist.printlist()

print()
print("after delMiddle operation")
llist.delMiddle(2.1)
llist.printlist()
