class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i]=time[i]%60
        d=Counter(time)
        ans=0
        for key in d:
            val=d[key]
            if key==0 or key==30:
                ans+=(val*(val-1))//2
            elif 60-key in d:
                ans+=(val*d[60-key])/2
        return int(ans)