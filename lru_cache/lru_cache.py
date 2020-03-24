from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.lis = DoublyLinkedList()
        self.size = 0
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache:
            out = self.cache[key]
            self.lis.move_to_front(out)
            return out.value[1]
        else:
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.cache:
            # If key already in cache we move it to the front
            inp = self.cache[key]
            # and replace the value
            inp.value = (key, value)
            self.lis.move_to_front(inp)
            return inp
        
        if self.size is self.limit:
            # If list length has reached its limit, remove last entry
            # This line will remove it from linked list by calling 
            # remove_from_tail, then pop from dict cache
            self.cache.pop(self.lis.remove_from_tail()[0])
            self.size -=1
        # ELSE
        self.lis.add_to_head((key, value))
        self.cache[key] = self.lis.head
        self.size += 1