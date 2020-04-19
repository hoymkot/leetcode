# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = [] 
        self.last = -1;
        
    def push(self, x: int) -> None:
        self.q1.append(x)
        self.last = x;

    def copypop(self, left, right) -> None:
        while len(left) > 1:
            right.append(left[0]);
            del left[0]
        r = left[0]
        del left[0];
        if (len(right) > 0 ):
            self.last = right[-1];
        return r;
        
    def pop(self) -> int:
        if len(self.q1) == 0:
            return self.copypop(self.q2, self.q1);
        return self.copypop(self.q1, self.q2);        

    def top(self) -> int:
        return self.last

    def empty(self) -> bool:
        return len(self.q1) + len(self.q2) == 0

