class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        operation='+'
        char=''
        num=0
        for i in range(len(s)):
            char=s[i]
            if char.isdigit():
                num=(num*10)+int(char)
            if (not char.isdigit() and char!=' ') or i==len(s)-1:
                if operation=='+':
                    stack.append(num)
                elif operation=='-':
                    stack.append(-num)
                elif operation=='*':
                    stack.append(stack.pop()*num)
                elif operation=='/':
                    a=stack.pop()
                    b=a/num
                    if b<0:
                        stack.append(math.ceil(b))
                    else:
                        stack.append(math.floor(b))
                operation=char
                num=0
        return sum(stack)