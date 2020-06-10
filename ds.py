# Implementing data structures in Python


class Stack:
    '''
    Implementing a simple stack in Python. Only allows push, pop, peek, and size functions
    LIFO: last in, first out
    '''

    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except:
            print('Error (pop): stack is empty')

    def peek(self):
        try:
            return self.stack[-1]
        except:
            print('Error (peek): stack is empty')

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


class Queue:
    '''
    Implementing a simple queue in Python. Only allows queue, dequeue, peek, and size functions
    FIFO: first in, first out
    '''

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        try:
            return self.queue.pop(0)
        except:
            print('Error (dequeue): queue is empty')

    def peek(self):
        try:
            return self.queue[0]
        except:
            print('Error (peek): queue is empty')

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


class TreeNode:
    '''
    Implementing a simple binary tree node in Python. Allows insert and remove functions that follow binary search tree properties.
    '''

    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # binary search tree insert
    def insert(self, data):
        if self:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self = TreeNode(data)

    # binary search tree remove (replace and remove)
    def remove(self, data):
        # if self is the node to remove
        if self.data == data:
            # if both left and right children exist, replace using minimum value in right subtree
            if self.left and self.right:
                temp = self.right
                while temp.left:
                    temp = temp.left
                self.data = temp.data
                # delete minimum value in right subtree
                self.right.remove(self.data)
            else:
                # if only a left child exists, replace using left child
                if self.left:
                    return self.left
                # if only a right child exists, replace using right child
                elif self.right:
                    return self.right
                # if leaf node, return None
                return
        # continue searching for the node to remove
        else:
            if self.data > data:
                self.left = self.left.remove(data)
            elif self.data < data:
                self.right = self.right.remove(data)
        return self

    # uses reverse in-order traversal
    def print_horizontal(self, depth=0):
        if self.right is not None:
            self.right.print_horizontal(depth + 1)
        
        print(('    ' * depth) + str(self.data))

        if self.left is not None:
            self.left.print_horizontal(depth + 1)


class MinHeap:
    '''
    Implementing a min-heap in Python. 
    Min-heap property: the value of a node is less than or equal to the values of its child nodes.
    Shape property: a nearly complete or complete binary tree
    '''

    # parent(i) = i // 2
    # left(i) = 2i
    # right(i) = 2i + 1
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.perc_up(self.size)

    # percolate up a newly inserted value to its correct position
    def perc_up(self, i):
        while i // 2 > 0:
            # if child is less than its parent
            if self.heap[i] < self.heap[i // 2]:
                # swap child and parent
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temp
            # update index
            i //= 2

    # return minimum without removing
    def peek(self):
        try:
            return heap[1]
        except:
            print('Error (peek): heap is empty')

    # remove and return minimum
    def extract(self):
        try:
            retval = self.heap[1]
        except:
            print('Error (extract): heap is empty')
            return

        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.perc_down(1)
        return retval

    # percolate down a value to its correct position
    def perc_down(self, i):
         # while not a leaf node
        while i * 2 <= self.size():
            mc_i = self.min_child_index(i)
            # if parent is greater than its smaller child
            if self.heap[i] > self.heap[mc_i]:
                # swap parent and smaller child
                temp = self.heap[i]
                self.heap[i] = self.heap[mc_i]
                self.heap[mc_i] = temp
            i = mc_i

    # return index of minimum (smaller) child
    def min_child_index(self, i):
        # if right child index is out of range
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            # if left child is less than right child
            if self.heap[2 * i] < self.heap[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1
