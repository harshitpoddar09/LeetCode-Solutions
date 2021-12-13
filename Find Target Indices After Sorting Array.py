class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        nums.sort()
        flag=1
        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i)
                flag=0
            if flag==0 and nums[i]!=target:
                break
        return ans