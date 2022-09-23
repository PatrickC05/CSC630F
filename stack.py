"""
Despite coding in Python for quite a few years, I never realized that lists in python are really stacks.
The basic functions are just renamed in the built-in python list: push vs append for adding an element,
size vs len for getting the number of elements, and peek for getting the most recent elements.
Pop (for removing and returning the last element) removes the same. However, it's also interesting that
the last in first out nature is removed from python lists. In stacks, you aren't able to remove elements
midway through the list, whereas you can in Python lists.

Reading more, I realized that append in list is actually an O(n) operation, whereas push in stack is O(1).
As an alternative, Python has a built-in library called LifoQueue, which implements a data structure more
similar to a stack.
"""

class Stack():
    def __init__(self):
        self.items = []
        self.top = None
    
    def push(self, item):
        self.items.append(item)
        self.top = item
    
    def pop(self):
        l = self.items.pop()
        self.top = self.items[-1]
        return l

    def isEmpty(self):
        return self.size() == 0
    
    def peek(self):
        return self.top
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()
    print(str(s.isEmpty()) + " (expected True)")
    try:
        print(s.pop())
    except:
        print("expected pop error")
    s.push(1)
    s.push(2)
    s.push(3)
    print(str(s.size()) + " (expected 3)")
    print(str(s) + " (expected [1, 2, 3])")
    print(str(s.pop()) + " (expected 3)")
    print(str(s) + " (expected [1, 2])")
    print(str(s.peek()) + " (expected 2)")
    print(str(s.isEmpty()) + " (expected False)")