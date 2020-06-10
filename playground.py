#!/usr/bin/env python

# Playground for data structures in Python


import ds


def test_stack():
    s = ds.Stack()
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(7)
    print(f't -> stack: {str(s)} (top)')
    print(f't -> peek() returns: {s.peek()}')
    print(f't -> size() returns: {s.size()}')
    s.pop()
    s.pop()
    print(f'stack: {s} (top)')
    print(f'pop() returns: {s.pop()}')
    s.pop()
    print(f'@ stack: {s} (top)')
    print(f'@ peek() returns: {s.peek()}')
    print(f'@ pop() returns: {s.pop()}')


def test_queue():
    q = ds.Queue()
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(8)
    print(f'queue: (front) {q} (back)')
    print(f'peek() returns: {q.peek()}')
    print(f'size() returns: {q.size()}')
    q.dequeue()
    q.dequeue()
    print(f'queue: (front) {q} (back)')
    print(f'dequeue() returns: {q.dequeue()}')
    q.dequeue()
    print(f'queue: (front) {q} (back)')
    print(f'peek() returns: {q.peek()}')
    print(f'dequeue() returns: {q.dequeue()}')


def test_bst():
    nums = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    root = ds.TreeNode(nums[0])
    for i in nums[1:]:
        root.insert(i)
    print(nums)
    root.print_horizontal()
    print('removing(3), should be replaced with 4')
    root.remove(3)
    root.print_horizontal()
    print('removing(13), should be replaced with None')
    root.remove(13)
    root.print_horizontal()


# playground
def main():
    print('testing stack. . .')
    test_stack()
    print()
    print('testing queue. . .')
    test_queue()
    print()
    print('testing binary search tree. . .')
    test_bst()


if __name__ == '__main__':
    main()
