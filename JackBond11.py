    def delete(self, head):
        if head.prev != None:
            head.prev.next = head.next
        else:
            self.head = head.next
        if head.next != None:
            head.next.prev = head.prev
        else:
            self.tail = head.prev
