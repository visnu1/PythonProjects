class Node:

    def __init__(self, element, size):
        self.data = element
        self.next = None
        self.position = size


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        node = Node(data, self.size)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        self.size += 1

    def print(self):
        arr = []
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp:
                arr.append(temp.data)
                temp = temp.next
            return arr

    def add_ordered(self, element):

        prev = None
        node = Node(element, self.size)
        temp = self.head
        self.size += 1
        if self.head is None:
            self.head = node
        else:

            while temp.data < element:
                if temp.next is None:
                    break
                prev = temp
                temp = temp.next
        if prev is None:
            if self.head.data < element:
                self.head.next = node
            else:
                node.next = temp
                self.head = node
        else:
            if temp.data > element:
                prev.next = node
                node.next = temp
            else:
                temp.next = node
        self.reposition()

    def reposition(self):
        temp = self.head
        index = 0
        while temp is not None:
            temp.position = index
            temp = temp.next
            index += 1

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def search(self, element):
        temp = self.head
        while temp.next:
            if temp.data == element:
                return True
            temp = temp.next
        return False

    def remove(self, element):
        temp = self.head
        prev = None
        while temp is not None:
            if temp.data == element:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                self.size -= 1
                self.reposition()
                return temp.data

            prev = temp
            temp = temp.next
        return -1

    def get_index(self, element):
        temp = self.head
        while temp.next:
            if temp.data == element:
                return temp.position
            temp = temp.next
        return -1


class Stack:

    def __init__(self):
        self.size = 0
        self.arr = []

    def push(self, item):
        self.arr.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.arr.pop()

    def peek(self):
        if self.size == 0:
            return None
        return self.arr[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size


class Queue:

    def __init__(self):
        self.arr = []
        self.size = 0

    def en_queue(self, item):
        self.arr.append(item)
        self.size += 1

    def de_queue(self):
        if self.size == 0:
            return None
        self.size -= 1
        deleted_element = self.arr[0]
        del self.arr[0]
        return deleted_element

    def peek(self):
        if self.size == 0:
            return None
        return self.arr[0]

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size


class DeQueue:

    def __init__(self):
        self.arr = []
        self.size = 0

    def add_front(self, item):
        self.arr.append(item)
        self.size += 1

    def add_rear(self, item):
        self.arr.insert(0, item)
        self.size += 1

    def remove_front(self):
        if self.size is 0:
            return None
        self.size -= 1
        return self.arr.pop()

    def remove_rear(self):
        if self.size == 0:
            return None
        self.size -= 1
        del_element = self.arr[0]
        del self.arr[0]
        return del_element

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def print(self):
        print(self.arr)
