class Solution:
    def reverse(self, x: int) -> int:
        minimum=-(2**31)
        maximum=(2**31)-1
        x=str(x)
        num=[]
        for i in x:
            num.append(i)
        num.reverse()
        if int(x)<0:
            num.pop()
            num.insert(0,'-')
        reverse_num=''.join(num)
        if int(reverse_num)>maximum or int(reverse_num)<minimum:
            return 0
        else:
            return int(reverse_num)