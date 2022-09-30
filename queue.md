# Queues

Similar to a queue in real life, a queue is a data structure where elements are removed in the same order that they are added. Elements are added in the back and removed from the front. This is known at first in first out (FIFO), and distinguishes queues from stacks, which are last in first out (LIFO).

## Terminology
There are two terms used to describe element positions. "Head" refers to the front of the queue, and the first element in line to be removed. "Tail" refers to the last element of the queue, or the most recently added element.

## Queue Methods
Aside from initialization, there are two main methods in queues. The enqueue method is similar to insert, adding an element to the front of the queue. The dequeue method is similar to pop, removing an element. However, instead of removing from the front like stacks, queues remove from the back.