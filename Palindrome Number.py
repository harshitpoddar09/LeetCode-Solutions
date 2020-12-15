class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Method 1 - 76 ms
        original_num=[]
        for i in str(x):
            original_num.append(i)
        reverse_num=[]
        for i in str(x):
            reverse_num.append(i)
        reverse_num.reverse()
        if original_num!=reverse_num:
            print('false')
        else:
            return 'true'
        
        #Method 2 - 44ms 
        return str(x)==str(x)[::-1]
        
        #Method 3 - without converting int to str
        ori_x=x
        if x>=0:
            rev_x=0
            for i in range(len(str(x))-1,-1,-1):
                a=x%10
                x=x//10
                rev_x+=a*(10**i)
            if ori_x==rev_x:
                return 'true'
            else:
                print('false')
        else:
            print('false')
