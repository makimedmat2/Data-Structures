"""
This file includes three classes: UnorderedList one class Node,
which we need to create former class.
"""

class Node:  # class node, needed to create list class

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        if self.isEmpty():
            raise ValueError(
                'The list is empty - you cannot delate this argument')

        if item > self.size():
            raise IndexError('Index out of range')

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __str__(self):
        current = self.head
        found = False
        k = ''

        if current == None:
            return '[' + k + ']'

        while not found:
            if current.getNext() == None:
                k = k + str(current.getData())
                return '[' + k + ']'
            else:
                k = k + str(current.getData()) + ', '
                current = current.getNext()

    def append(self, item):
        current = self.head
        found = False
        if self.isEmpty() == True:
            self.add(item)
        else:
            while not found:
                if current.getNext() == None:
                    current.setNext(Node(item))
                    found = True
                else:
                    current = current.getNext()

    def index(self, item):
        current = self.head
        found = False
        currentPos = 0
        if self.isEmpty() == True:
            raise ValueError('The list is empty!!')

        if self.search(item) == False:
            raise ValueError('This object is not in this list')
        while not found:
            if current.getData() == item:
                found = True
            else:
                currentPos += 1
                current = current.getNext()
        return currentPos

    def position(self, inx):
        current = self.head
        while True:
            if self.index(current.getData()) == inx:
                return current
            else:
                current = current.getNext()

    def insert(self, pos, item):
        if self.isEmpty() == True:
            raise IndexError('Index out of range - the list is empty')

        if pos > self.size():
            raise IndexError('Index "pos" out of range')

        prev = pos-1

        if self.position(prev).getNext() == None:
            self.append(item)

        current = self.position(pos-1)
        newnext = current.getNext()
        new = Node(item)
        current.setNext(new)
        new.setNext(newnext)

    def pop(self, pos=None):
        current = self.head
        found = False
        if pos != None:
            if pos == 0:
                temp = current.getNext()
                self.head = temp
                return current.getData()
            else:
                current = self.position(pos-1)
                temp = current.getNext()
                new = temp.getNext()
                if current.getNext() != None:
                    current.setNext(new)
                    return temp.getData()

        else:
            while True:
                temp = current.getNext()
                if temp.getNext() == None:
                    current.setNext(None)
                    return temp.getData()
                else:
                    current = temp

    def __len__(self):
        return self.size()

    def __getitem__(self, pos):
        current = self.head
        currentPos = 0
        if pos > len(self)-1:
            raise IndexError('Index out of range')
        while currentPos < pos:
            current = current.getNext()
            currentPos += 1
        return current.getData()
