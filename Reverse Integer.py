# Method 1
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

# Method 2
class Solution:
    def reverse(self, x: int) -> int:
        minimum=-(2**31)
        maximum=(2**31)-1
        if x<0:
            reverse_num=int(str(x)[:0:-1])*(-1)
        else:
            reverse_num=int(str(x)[::-1])
        if reverse_num>maximum or reverse_num<minimum:
            return 0
        return reverse_num
