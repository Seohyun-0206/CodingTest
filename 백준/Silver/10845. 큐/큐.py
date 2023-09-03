import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.cnt = 0

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        node = Node(data)

        if self.isEmpty(): #원소가 하나도 없다면
            self.front = self.rear = node #시작과 끝은 새 노드로
        else:
            self.rear.next = node # 원래 끝의 다음을 새 노드로
            self.rear = node #새 노드를 끝으로 설정

        self.cnt += 1

    def dequeue(self):
        if self.isEmpty():
            return -1

        node = self.front #삭제할 노드
        if self.front == self.rear: #원소가 한개였다면
            self.front = self.rear = None #시각과 끝을 모두 None으로
        else: #다른 원소가 더 존재한다면
            self.front = self.front.next #시작의 다음을 시작으로

        self.cnt -= 1
        return node.data

    def size(self):
        return self.cnt

    def fro(self):
        if self.isEmpty():
            return -1

        return self.front.data

    def back(self):
        if self.isEmpty():
            return -1

        return self.rear.data

import sys
n = int(input())

queue = Queue()

for i in range(n):
    op = sys.stdin.readline().split()

    if op[0] == "push":
        queue.enqueue(op[1])
    elif op[0] == "pop":
        print(queue.dequeue())
    elif op[0] == "size":
        print(queue.size())
    elif op[0] ==  "empty":
        if queue.isEmpty():
            print(1)
        else:
            print(0)
    elif op[0] == "front":
        print(queue.fro())
    elif op[0] == "back":
        print(queue.back())



