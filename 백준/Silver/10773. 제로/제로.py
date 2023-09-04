class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList_Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        node = Node(data)

        if self.isEmpty(): #원소가 하나도 없다면
            self.top = node
        else:
            node.next = self.top
            self.top = node #새로운 노드가 가장 앞에 들어가는 것(head)

    def pop(self):
        if self.isEmpty():
            return None

        node = self.top
        self.top = node.next #top 원소가 삭제

        return node.data

    def peek(self):
        if self.isEmpty():
            return None

        return self.top.data

k = int(input())
result = 0

stack = LinkedList_Stack()
for i in range(k):
    n = int(input())

    if n == 0:
        result -= stack.pop()
    else:
        stack.push(n)
        result += n

print(result)