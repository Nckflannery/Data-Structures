import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True
        elif target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        else:
            return None

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Breadth first so we want FIFO/LILO(queue)
        # Create queue
        que = Queue()
        current = node
        while current:
            print(current.value)
            if current.left:
                que.enqueue(current.left)
            if current.right:
                que.enqueue(current.right)
            current = que.dequeue()


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Depth first so we want FILO/LIFO(stack)
        # Create stack
        st = Stack()
        current = node
        while current:
            print(current.value)
            if current.right:
                st.push(current.right)
            if current.left:
                st.push(current.left)
            current = st.pop()

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(node)
        if self.right:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(node)
        if self.right:
            self.right.post_order_dft(node)
        print(self.value)
