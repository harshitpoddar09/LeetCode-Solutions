class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=nums[0]
        current_sum=0
        queue=[]
        for i in nums:
            if queue:
                if i>queue[-1]:
                    queue.append(i)
                    current_sum+=i
                else:
                    current_sum=i
                    queue=[i]
            else:
                queue.append(i)
                current_sum+=i
            ans=max(ans,current_sum)
        return ans