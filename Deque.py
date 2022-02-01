'''
A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front and a rear, and the items remain positioned in the collection.  In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure
'''

class Deque(object):
    def __init__(self):
        self.container = []

    def addfront(self, item):
        self.container.append(item)

    def addrear(self, item):
        self.container.insert(0, item)

    def removerear(self):
        if self.container == []:
            ErrorMessage = "Cannot remove from empty deque"
            return ErrorMessage
        else:
            return self.container.pop(0)

    def removefront(self):
        if self.container == []:
            ErrorMessage = "Cannot remove from empty deque"
            return ErrorMessage
        else:
            return self.container.pop()

    def is_Empty(self):
        if self.container == []:
            return True
        else:
            return False

    def size(self):
        return (len(self.container))

    def __repr__(self):
        return 'Elements in deque: {}'.format(self.container)

    def peek_front(self):
        return self.container[-1]

    def peek_rear(self):
        return self.container[0]

if __name__ == '__main__':
    test = Deque()
    print(test.size())
    print(test.is_Empty())
    print(test.removerear())
    print(test.removefront())
    test.addfront(1)
    test.addrear(2)
    test.addfront(3)
    test.addrear(1)
    test.addrear(5)
    test.addfront(9)
    print(test)
    print(test.peek_rear())
    print(test.peek_front())
    print(test.is_Empty())
    print(test.size())
    print(test.removerear())
    print(test.removefront())
    print(test)