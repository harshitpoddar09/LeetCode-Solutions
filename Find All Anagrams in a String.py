#Submission 2 - 148ms
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        k=len(p)
        p=Counter(p)
        cur_win=Counter(s[:k-1])
        w_start=0
        for w_end in range(k-1,len(s)):
            cur_win[s[w_end]]+=1
            if cur_win==p:
                ans.append(w_start)
            cur_win[s[w_start]]-=1
            if cur_win[s[w_start]]==0:
                del cur_win[s[w_start]]
            w_start+=1
        return ans

#Submission 1 - 7668ms
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        p=sorted(p)
        k=len(p)
        w_start=0
        cur_win=''
        for w_end in range(len(s)):
            cur_win+=s[w_end]
            if w_end>=k-1:
                if sorted(cur_win)==p:
                    ans.append(w_start)
                cur_win=cur_win[1:]
                w_start+=1
        return ans