class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums,k):
            w_start=0
            d={}
            count=0
            for w_end in range(len(nums)):
                if nums[w_end] not in d:
                    d[nums[w_end]]=0
                d[nums[w_end]]+=1
                while len(d)>k:
                    d[nums[w_start]]-=1
                    if d[nums[w_start]]==0:
                        del d[nums[w_start]]
                    w_start+=1
                count+=w_end-w_start+1
            return count
        return atMostK(nums,k)-atMostK(nums,k-1)