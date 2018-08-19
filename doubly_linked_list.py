class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None
    
    def get(self):
        return self.val
    
    def get_next(self):
        return self.next
    
    def set_next(self, val):
        self.next = val

    def get_previous(self):
        return self.previous

    def set_previous(self, val):
        self.previous = val

class DLL(object):

    def __init__(self, head=None):
        self.head = head
    
    def insert(self, val):
        new_node = Node(val)
        new_node.set_previous(self.head)
        if self.head:
            self.head.set_next(new_node)
        self.head = new_node


    @property
    def len(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_previous()
        return count



    def get_previous(self, val):
        current = self.head
        while current:
            if current.get() == val:
                previousval = current.get_previous()
                if previousval:
                    return previousval.get()
                else:
                    return None
            current = current.get_previous()
        raise ValueError ("The value does not exist")


    def get_next(self, val):
        current = self.head
        while current:
            if current.get() == val:
                nextval = current.get_next()
                if nextval:
                    return nextval.get()
                else:
                    return None
            current = current.get_previous()
        raise ValueError ("The value does not exist")


   
    def add_previous(self, existval, newval):
        current = self.head 
        while current:
            if current.get() == existval:
                new_node = Node(newval)
                existing_previous = current.get_previous()
                if existing_previous:
                    new_node.set_previous(existing_previous)
                    existing_previous.set_next(new_node)
                new_node.set_next(current)
                current.set_previous(new_node)
                return           
            current = current.get_previous()
        raise ValueError ("The value does not exist")

    def delete(self, val):
        current = self.head 
        while current:
            if current.get() == val:
                print ("Hi")
                previous_node = current.get_previous()
                next_node = current.get_next() 
                if previous_node:
                    previous_node.set_next(next_node)
                if next_node:
                    next_node.set_previous(previous_node)
                return 
            current = current.get_previous()
        raise ValueError ("The value does not exist")
    

    def previous(self):
        current = self.head
        while current:
            yield current.get()
            current = current.get_previous()



    

if __name__ == "__main__":
    a = DLL()
    a.insert(2)
    a.insert(5)
    a.insert(10)
    a.insert(12)
    a.add_previous(10, 8)
    for i in a.previous():
        print (i)
    todelete = 8
    print ("Deleting ", todelete, "..")
    a.delete(8)
    for i in a.previous():
        print(i)