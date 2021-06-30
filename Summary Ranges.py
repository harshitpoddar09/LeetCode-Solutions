class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [str(nums[0])]
        i=0
        while i<len(nums)-1:
            start=nums[i]
            end=nums[i]
            while i<len(nums)-1 and nums[i+1]==nums[i]+1:
                end+=1
                i+=1
            ans.append([start,end])
            i+=1
        if nums[-1]-1!=nums[-2]:
            ans.append([nums[-1],nums[-1]])
        for i in range(len(ans)):
            if ans[i][0]==ans[i][1]:
                ans[i]=str(ans[i][0])
            else:
                ans[i]=str(ans[i][0])+'->'+str(ans[i][1])
        return ans