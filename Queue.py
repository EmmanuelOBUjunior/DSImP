class Queue:
    def __init__(self):
        self.container = []

    def enqueue(self, item):
        self.container.append(item)
    def dequeue(self):
        return self.container.pop(0)
    def peek(self):
        return self.container[0]
    def isEmpty(self):
        if self.container == []:
            return True
        return False

    def size(self):
        return len(self.container)

    def display(self):
        return self.container




# if __name__ == '__main__':
#     test = Queue()
#     print(test.isEmpty())
#     print(test.size())
#     print(test.display())
#     test.enqueue(1)
#     test.enqueue(2)
#     test.enqueue(3)
#     test.enqueue(4)
#     test.enqueue(20)
#     print(test.isEmpty())
#     print(test.size())
#     print(test.display())
#     print(test.peek())
#     print(test.dequeue())
#     print(test.display())
#     print(test.size())
