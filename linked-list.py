class LinkedList(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)
    
    def __len__(self):
        if not self.next:
            return 1
        return 1 + len(self.next)

    def search(self, target):
        if self.data == target:
            return self

        if not self.next:
            return None

        return self.next.search(target)

    def prepend(self, new):
        # Insert new element (LinkedList class) before self
        new.next = self
        new.prev = self.prev
        if self.prev:
            self.prev.next = new
        self.prev = new
        return new
    
    def insert(self, new):
        # Insert new element (LinkedList class) after self
        new.next = self.next
        new.prev = self
        if self.next:
            self.next.prev = new
        self.next = new
        return

    def delete(self):
        # Delete self
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return

def printList(start):
    print(start)
    if start.next:
        printList(start.next)

if __name__ == "__main__":
    doesNotContainFish = LinkedList("Dog")
    print("search fails: {}".format(doesNotContainFish.search("Fish")))

    containsFish = LinkedList("Fish")
    print("search succeeds: {}".format(containsFish.search("Fish")))

    animals = LinkedList("Dog")
    animals = animals.prepend(LinkedList("Gunga"))

    printList(animals)
    print("Expected: Gunga Dog")
    print("Length: {} (2 expected)".format(len(animals)))
    print('---')

    animals.insert(LinkedList("Cat"))
    animals.insert(LinkedList("Fish"))

    printList(animals)
    print("Expected: Gunga Fish Cat Dog")
    print("Length: {} (4 expected)".format(len(animals)))
    print('---')

    fish = animals.search("Fish")

    bird = LinkedList("Bird")
    fish.insert(bird)
    horse = LinkedList("Horse")
    bird.insert(horse)
    
    fish.delete()
    printList(animals)
    print("Expected: Gunga Bird Horse Cat Dog")
    print("Length: {} (5 expected)".format(len(animals)))