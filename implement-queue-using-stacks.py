# https://leetcode.com/problems/implement-queue-using-stacks
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []        
        

    def push(self, x: int) -> None:
        self.stack1.append(x);
        

    def pop(self) -> int:
        if (len(self.stack2) > 0):
            return self.stack2.pop()
        while len(self.stack1) > 0: 
            self.stack2.append(self.stack1.pop());        
        return self.stack2.pop();
            

    def peek(self) -> int:
        r = self.pop()
        self.stack2.append(r);
        return r;
        

    def empty(self) -> bool:
        return len(self.stack1) + len(self.stack2) == 0;
