class Queue():
    def __init__(self):
        self.items = []
        self.head = None
        self.tail = None

    def enqueue(self, item):
        self.items.append(item)
        self.head = self.items[0]
        self.tail = item

    def dequeue(self):
        l = self.items.pop(0)
        if self.items:
            self.head = self.items[0]
        else:
            self.head = None
            self.tail = None
        return l

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(str(q.dequeue()) + " (expected 1)")
    print(str(q.dequeue()) + " (expected 2)")
    q.enqueue(4)
    print(str(q.dequeue()) + " (expected 3)")
    print(str(q.dequeue()) + " (expected 4)")