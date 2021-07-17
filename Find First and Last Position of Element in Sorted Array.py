#Submission 1 - 104ms
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                ans=[i,i+nums.count(target)-1]
                break
        return ans

#Submission 2 - 92ms
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        if nums.count(target)==0:
            ans=[-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    ans=[i,i+nums.count(target)-1]
                    break
        return ans

#Submission 3 - 80ms
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo=0
        hi=len(nums)-1
        idx=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                idx=mid
                break
            elif nums[mid]>target:
                hi=mid-1
            else:
                lo=mid+1
        if idx==-1:
            return [-1,-1]
        i=idx
        j=idx
        while i>-1 and nums[i]==target:
            i-=1
        while j<len(nums) and nums[j]==target:
            j+=1
        return [i+1,j-1]
