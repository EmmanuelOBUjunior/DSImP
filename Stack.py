'''
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.
'''
class Stack(object):
    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return (len(self.container))

    def isEmpty(self):
        if self.container == []:
            return True
        else:
            return False

    def __repr__(self):
        return 'Elements in Stack: {}'.format(self.container)

if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    print(stack.size())
    print(stack)
    stack.push(2)
    stack.push(5)
    stack.push(12)
    stack.push(78)
    stack.push(10)
    print(stack)
    print(stack.peek())
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.peek())
    print(stack)