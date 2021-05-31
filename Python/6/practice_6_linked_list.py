from practice_6_event_manager import EventManager


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.eventManager = EventManager()
        self.head = None

    def Insert(self, position, value):
        counter = 0
        if self.head:
            current = self.head
            while current.next:
                if counter == position:
                    break
                current = current.next
                counter += 1
            nodes = current.next
            current.next = Node(value)
            current = current.next
            current.next = nodes

        else:
            self.head = Node(value)
        self.eventManager.event("add", {"new value": value, "position": position, "result list": self.__str__()})

    def __str__(self):
        string = ''
        if self.head:
            string += '['
            current = self.head
            while current.next:
                string += str(current.data) + ","
                current = current.next
            string += str(current.data)
            string += ']'
        else:
            string = 'List is empty'
        return string

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
            if len(value_in_string) == 4:
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

    def Remove(self, position):
        counter = 0
        temp = self.head
        deleted_value = 0
        prev = None
        if temp is not None:
            if counter == position:
                deleted_value = self.head.data
                self.head = temp.next
                self.eventManager.event("remove",
                                        {"deleted value": deleted_value, "position": position,
                                         "result list": self.__str__()})
                return

        while temp is not None:
            if position == counter:
                deleted_value = temp.data
                break
            prev = temp
            temp = temp.next
            counter += 1

        if temp is None:
            return
        prev.next = temp.next
        self.eventManager.event("remove",
                                {"deleted value": deleted_value, "position": position, "result list": self.__str__()})

    def RemoveNodes(self, begin, end):
        for i in range(begin, end):
            self.Remove(begin)
