class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.Head = None

    def insert(self, data):
        new_node = Node(data)
        if self.Head is None:
            self.Head = new_node
        else:
            take = self.Head
            while take.next is not None:
                take = take.next
            take.next = new_node

    def delete(self, data):
        prv = None
        nxt = None
        take = self.Head

        if take is not None:
            if take.data == data:
                if take.next is not None:
                    nxt = take.next
                    take = None
                    self.Head = nxt
                else:
                    take = None

        while take is not None:
            if take.data == data:
                if take.next is not None:
                    nxt = take.next
                    prv.next = nxt
                    break
                else:
                    prv.next = None
                    break
            prv = take
            take = take.next

    def print(self):
        take = self.Head
        while take is not None:
            print(take.data)
            take = take.next


if __name__ == '__main__':
    A = LinkedList()
    A.insert(10)
    A.insert(20)
    A.insert(30)
    A.insert(40)
    A.print()
    A.delete(30)
    print('After deleting a node from linked list: \n')
    A.print()
    A.delete(40)
    print('After deleting a node from linked list: \n')
    A.print()
    print('After adding a node from linked list: \n')

    A.insert(400)
    A.print()
