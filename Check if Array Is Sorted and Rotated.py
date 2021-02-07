class Solution:
    def check(self, nums: List[int]) -> bool:
        a=[]
        for i in nums:
            a.append(i)
        a.sort()
        b=[1]*len(a)
        ans=0
        for p in range(len(a)):
            for q in range(len(a)):
                b[(q+p)%len(a)]=a[q]
            if b==nums:
                ans=1
                break
        return ans