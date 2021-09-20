class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        ans=0
        for i in nums_set:
            if i-1 not in nums_set:
                cur_num=i
                cur_len=1
                while cur_num+1 in nums_set:
                    cur_num+=1
                    cur_len+=1
                ans=max(ans,cur_len)
        return ans