class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index1=[]
        for i in range(len(nums)):
            if nums[i]==1:
                index1.append(i)
        ans=1
        for j in range(1,len(index1)):
            diff=index1[j]-index1[j-1]
            if diff<k+1:
                ans=0
                break
        return ans