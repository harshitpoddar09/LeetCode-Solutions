class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        imax=-1
        imin=-1
        curmax=-float('inf')
        curmin=float('inf')
        for i in range(len(nums)):
            if nums[i]>curmax:
                imax=i
                curmax=nums[i]
            if nums[i]<curmin:
                imin=i
                curmin=nums[i]
        fmax=True
        if imax+1>len(nums)-imax:
            fmax=False
        fmin=True
        if imin+1>len(nums)-imin:
            fmin=False
        a=min(imax+1,len(nums)-imax)
        b=min(imin+1,len(nums)-imin)
        ans=0
        if a<b:
            ans+=a
            if fmax:
                nums=nums[a:]
            else:
                nums=nums[:len(nums)-a]
            idx=nums.index(curmin)
            ans+=min(idx+1,len(nums)-idx)
        else:
            ans+=b
            if fmin:
                nums=nums[b:]
            else:
                nums=nums[:len(nums)-b]
            idx=nums.index(curmax)
            ans+=min(idx+1,len(nums)-idx)
        return ans