class Solution:
    def isValid(self, s: str) -> bool:
        open_b=['{','(','[']
        stack=[]
        for i in s:
            if i in open_b:
                stack.append(i)
            else:
                if len(stack)==0:
                    return 0
                a=stack.pop()
                if a=='{' and i!='}':
                    return 0
                elif a=='(' and i!=')':
                    return 0
                elif a=='[' and i!=']':
                    return 0
        if len(stack)!=0:
            return 0
        return 1