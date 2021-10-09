import time
import turtle
import drawing_builder as db


class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def set_data(self, data):
        self.data = data

    def clear(self):
        self.data = None
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
        self.height = 50

    def add(self, val):
        curr = self.head
        while curr.get_next() is not None:
            curr = curr.next
        newNode = Node(data=val)
        curr.set_next(newNode)
        newNode.set_prev(curr)
        self.size += 1

    def get_size(self):
        return self.size

    def Empty(self):
        return self.get_size() == 1

    def get_index(self, val):
        index = 0
        curr = self.head.get_next()
        while curr is not None:
            if curr.get_data() == val:
                return index
            index += 1
            curr = curr.get_next()
        return -1

    def get(self, index):
        count = 0
        curr = self.head.get_next()
        while curr is not None:
            if count == index:
                return curr
            count += 1
            curr = curr.get_next()
        return None

    def remove(self, val):
        curr = self.head.get_next()
        while curr is not None:
            if curr.get_data() == val:
                prev = curr.get_prev()
                prev.set_next(curr.get_next())
                next = curr.get_next()
                next.set_prev(prev)
                curr.clear()
                return
            curr = curr.get_next()

    def remove_index(self, index):
        curr = self.head.get_next()
        i = 0
        while curr is not None:
            if i == index:
                prev = curr.get_prev()
                prev.set_next(curr.get_next())
                next = curr.get_next()
                next.set_prev(prev)
                curr.clear()
                return
            i += 1
            curr = curr.get_next()

    def draw(self):
        drawing = turtle.Turtle()
        drawing.speed(10)

        db.square(drawing, self.height)
        drawing.write("Header", False, align='center')
        curr = self.head.get_next()
        while curr is not None:
            db.square(drawing, self.height)
            # draw value in the middle of the square
            db.write_text(drawing, curr.get_data(), self.height / 2)
            curr = curr.get_next()
        time.sleep(10)


test = DoublyLinkedList()
for i in range(5):
    test.add(i)
test.draw()
