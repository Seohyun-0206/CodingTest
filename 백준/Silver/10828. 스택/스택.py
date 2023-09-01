class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList_Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        node = Node(data)

        if self.isEmpty(): #원소가 하나도 없다면
            self.top = node
        else:
            node.next = self.top
            self.top = node #새로운 노드가 가장 앞에 들어가는 것(head)

        self.count += 1

    def pop(self):
        if self.isEmpty():
            return -1

        node = self.top
        self.top = node.next #top 원소가 삭제

        self.count -= 1
        return node.data

    def peek(self):
        if self.isEmpty():
            return -1

        return self.top.data

    def size(self):
        return self.count

import sys

n = int(input())

stack = LinkedList_Stack()

for i in range(n):
    op = sys.stdin.readline().split()

    if op[0] == 'push':
        stack.push(op[1])
    elif op[0] == 'pop':
        print(stack.pop())
    elif op[0] == 'size':
        print(stack.size())
    elif op[0] == 'empty':
        if stack.isEmpty():
            print(1)
        else:
            print(0)
    elif op[0] == 'top':
        print(stack.peek())
