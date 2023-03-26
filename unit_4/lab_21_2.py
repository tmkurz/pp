class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

for i in range(1, 101):
    stack1.push(i)

for i in range(100):
    stack2.push(stack1.pop())

for i in range(100):
    stack3.push(stack2.pop())





