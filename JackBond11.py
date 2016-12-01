#class for node objects. OOP
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

#class for list object. OOP
class List(object):
    #Initialization
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, head, num):
        if head != None:
            num.next = head.next
            head.next = num
            num.prev = num
            if num.next != None:
                num.next.prev = num
        if self.head == None:
            self.head = self.tail = num
            num.prev = num.next = None
        elif self.tail == head:
            self.tail = num

    #Node delete function
    def delete(self, head):
        if head.prev != None:
            head.prev.next = head.next
        else:
            self.head = head.next
        if head.next != None:
            head.next.prev = head.prev
        else:
            self.tail = head.prev

    #function to print tree in readable format. uses list             
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print("List: ",",".join(values))

#allows for progrma to run, with testing nodes and function use
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head,Node(10))
    l.insert(l.head,Node(12))
    #remove below comment to run delete function
    #l.delete(l.head)
    l.display()
