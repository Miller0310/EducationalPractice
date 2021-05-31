class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Insert(self, value):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)

    def Print(self):
        if self.head:
            print('[', end='')
            current = self.head
            while current.next:
                print(current.data, ",", end='', sep='')
                current = current.next
            print(current.data, ']', sep='')
        else:
            print("List is empty")

    def Swap(self):
        current = self.head
        prev = None
        while current:
            value_in_string = str(current.data)
            if (int(value_in_string[0]) + int(value_in_string[1])) == (
                    int(value_in_string[2]) + int(value_in_string[3])):
                new_value = value_in_string[1] + value_in_string[0] + value_in_string[3] + value_in_string[2]
                current.data = int(new_value)
                if prev is None:
                    prev = current
                    current = current.next
                else:
                    value = current.data
                    current.data = prev.data
                    prev.data = value
                    current = current.next
            else:
                current = current.next
