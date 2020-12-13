class Solution:
    def isPalindrome(self, x: int) -> bool:
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