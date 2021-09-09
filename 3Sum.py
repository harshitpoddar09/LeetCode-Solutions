#Submission 2 - 988ms
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                a=nums[l]+nums[r]
                if a==-nums[i]:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif a<-nums[i]:
                    l+=1
                else:
                    r-=1
        return ans

#Submission 1 - 4816ms
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        n=len(nums)
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                a=nums[l]+nums[r]
                if a==-nums[i]:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif a<-nums[i]:
                    l+=1
                else:
                    r-=1
        return ans