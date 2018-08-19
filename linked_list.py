class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def get(self):
        return self.val
    
    def get_next(self):
        return self.next
    
    def set_next(self, val):
        self.next = val

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data): 
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    @property
    def len(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def search(self, val):
        current = self.head
        loc = 0
        while current:
            if current.get() == val:
                return loc
            loc += 1
            current = current.get_next()
        raise ValueError ('The value does not exist')

    def delete(self, val):
        current = self.head
        if current.get() == val:
            self.head = current.get_next()
            return
        last = current
        current = current.get_next()
        while current:
            if current.get() == val:
                current = current.get_next()
                last.set_next(current)
                return 
            last = current
            current = current.get_next()
        raise ValueError('The value does not exist')

    def next(self):
        current = self.head
        while current:
            yield current.get()
            current = current.get_next()
        

            



if __name__ == "__main__":
    a = LinkedList()
    a.insert(5)
    a.insert(10)
    a.insert(7)
    a.insert(3)
    for i in a.next():
        print(i)
