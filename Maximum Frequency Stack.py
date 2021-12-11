class FreqStack:

    def __init__(self):
        self.freq={}
        self.stack={}
        self.maxf=0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val]=0
        self.freq[val]+=1
        f=self.freq[val]
        if f>self.maxf:
            self.maxf=f
        if f not in self.stack:
            self.stack[f]=[]
        self.stack[f].append(val)

    def pop(self) -> int:
        x=self.stack[self.maxf].pop()
        self.freq[x]-=1
        if not self.stack[self.maxf]:
            self.maxf-=1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()