class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for j in range(len(digits)-1,-1,-1):
            num=num+digits[j]*(10**(len(digits)-1-j))
        num=num+1
        ans=[]
        for i in str(num):
            ans.append(i)
        while len(ans)<len(digits):
            ans.insert(0,0)
        return ans