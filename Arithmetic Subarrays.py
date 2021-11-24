class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            cur=nums[l[i]:r[i]+1]
            cur.sort()
            if len(cur)<3:
                ans.append(True)
            else:
                diff=cur[1]-cur[0]
                for j in range(1,len(cur)-1):
                    if cur[j+1]-cur[j]!=diff:
                        ans.append(False)
                        break
                else:
                    ans.append(True)
        return ans