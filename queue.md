# Queues

Similar to a queue in real life, a queue is a data structure where elements are removed in the same order that they are added. Elements are added in the back and removed from the front. This is known at first in first out (FIFO), and distinguishes queues from stacks, which are last in first out (LIFO).

## Terminology
There are two terms used to describe element positions. "Head" refers to the front of the queue, and the first element in line to be removed. "Tail" refers to the last element of the queue, or the most recently added element.

## Queue Methods
Initialization is the first step to write the initalization method. We set the head and tail to `None`. In addition, the item is the empty list.
```python
def __init__(self):
    self.items = []
    self.head = None
    self.tail = None
```
Aside from initialization, there are two main methods in queues. The enqueue method is similar to insert, adding an element to the front of the queue. In addition, enqueue must update the tail method, since the inserted element is now at the back. 
```python
def enqueue(self, item):
    self.items.append(item)
    self.head = self.items[0]
    self.tail = item
```
The dequeue method is similar to pop, removing an element. However, instead of removing from the front like stacks, queues remove from the back.
```python
def dequeue(self):
    l = self.items.pop(0)
    if self.items:
        self.head = self.items[0]
    else:
        self.head = None
        self.tail = None
    return l
```

We must check if the new queue is empty before updating the head and tail. If the new queue is empty, we set both to `None`, as if it was just initialized.