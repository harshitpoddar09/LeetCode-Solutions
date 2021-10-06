#Submission 2 - 232ms 14.8mb
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cur_flips=0
        for i in s:
            if i=='0':
                cur_flips+=1
        ans=cur_flips
        for i in s:
            if i=='0':
                cur_flips-=1
            else:
                cur_flips+=1
            ans=min(cur_flips,ans)
        return ans

#Submission 1 - 376ms 17.3mb
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix_sums=[]
        n=len(s)
        cur=0
        for i in s:
            if i=='1':
                cur+=1
            prefix_sums.append(cur)
        ans=float('inf')
        cur_flip=float('inf')
        for i in range(n):
            cur_flip=(prefix_sums[i])+((n-(i+1))-(prefix_sums[-1]-prefix_sums[i])) #counting 1s till i and 0s after i
            ans=min(cur_flip,ans)
        ans=min(ans,min(cur,n-cur)) #all 0s or all 1s case
        return ans