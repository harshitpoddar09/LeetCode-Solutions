class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        cur_num=0
        cur_str=''
        for i in s:
            if i=='[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str=''
                cur_num=0
            elif i==']':
                num=stack.pop()
                prev_str=stack.pop()
                cur_str=prev_str+(num*cur_str)
            elif i.isdigit():
                cur_num=(cur_num*10)+int(i)
            else:
                cur_str+=i
        return cur_str