'''
A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer.
'''


class Node(object):
    def __init__(self, element=None, nextnode=None):
        self.data = element
        self.next = nextnode


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insertatbeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def display(self):
        if self.head is None:
            print('List is Empty')
        nextnode = self.head
        listelements = ''
        while nextnode:
            listelements += str(nextnode.data) + '-->'
            nextnode = nextnode.next
        print(listelements)

    def insertatend(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        nextNode = self.head
        while nextNode.next:
            nextNode = nextNode.next

        nextNode.next = Node(data, None)

    def insertvalues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertatend(data)

    def length(self):
        total = 0
        nextnode = self.head
        while nextnode:
            total += 1
            nextnode = nextnode.next
        return total

    def removeat(self, index):
        if index < 0 or index >= self.length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next

        count = 0
        nextnode = self.head
        while nextnode:
            if count  == index - 1:
                nextnode.next = nextnode.next.next
                break
            nextnode = nextnode.next
            count += 1


    def insertat(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insertatbeginning(data)
            return

        count = 0
        nextnode = self.head
        while nextnode:
            if count == index - 1:
                node = Node(data, nextnode.next)
                nextnode.next = node
                break

            nextnode = nextnode.next
            count +=1

if __name__ == '__main__':
    test = LinkedList()
    # test.display()
    # test.insertatbeginning(5)
    # test.insertatbeginning(45)
    # test.display()
    # test.insertatend(86)
    # test.insertatend(90)
    test.insertvalues(['banana', 'apple', 'grape', 'orange'])
    test.display()
    test.removeat(2)
    test.display()
    test.insertat(0, 'work')
    test.insertat(3, 'work')
    test.display()
    print(test.length())
