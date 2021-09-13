class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        w_start=0
        max_length=0
        c1=0
        for w_end in range(len(nums)):
            if nums[w_end]==1:
                c1+=1
            if w_end-w_start+1-c1>k:
                if nums[w_start]==1:
                    c1-=1
                w_start+=1
            max_length=max(max_length,w_end-w_start+1)
        return max_length