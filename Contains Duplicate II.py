class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        for i,value in enumerate(nums):
            if value in seen:
                if i-seen[value]<=k:
                    return True
                else:
                    seen[value]=i
            else:
                seen[value]=i
        return False