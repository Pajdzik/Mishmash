#https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

class MyQueue(object):
    def __init__(self):
        self.index = 0
        self.stack = []
    
    def peek(self):
        return self.stack[self.index]
        
    def pop(self):
        self.index += 1
        return self.stack[self.index - 1]
        
    def put(self, value):
        self.stack.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())