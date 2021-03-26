#Submission 2 (14.4mb)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=nums[:n]
        j=1
        for i in nums[n:]:
            ans.insert(j,i)
            j+=2
        return ans
    
    
#Submission 1 (14.5mb)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        a=nums[:n]
        b=nums[n:]
        for i in range(n):
            ans.append(a[i])
            ans.append(b[i])
        return ans
