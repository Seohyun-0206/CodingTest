class List_Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        empty = False
        if len(self.top) == 0:
            empty = True
        return empty

    def push(self, data):
        self.top.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        return self.top.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.top[-1]


while True:
    arr = input()
    stack = List_Stack()

    if arr == ".":
        break

    flag = 0
    for i in arr:
        if i == "(" or i == "[":
            stack.push(i)
        elif i == ")":
            if stack.peek() == "(":
                stack.pop()
            else:
                flag = 1
                break
        elif i == "]":
            if stack.peek() == "[":
                stack.pop()
            else:
                flag = 1
                break

    if flag == 0 and stack.isEmpty():
        print("yes")
    else:
        print("no")