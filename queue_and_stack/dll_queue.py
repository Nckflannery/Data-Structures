import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        ''' Add item to BACK of queue'''
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        '''Remove and return an item from the FRONT of the queue'''
        # If there is no list you have no items to return
        if self.size < 1:
            return None
        else:
            value = self.storage.remove_from_head()
            self.size -= 1
            return value

    def len(self):
        return self.size
