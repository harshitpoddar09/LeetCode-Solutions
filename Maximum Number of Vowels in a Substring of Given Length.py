#Submission 2 - 188 ms
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        w_start=0
        w_vowels=0
        ans=0
        for w_end in range(len(s)):
            w_vowels+=s[w_end] in vowels
            if w_end>=w_start+k-1:
                ans=max(ans,w_vowels)
                w_vowels-=s[w_start] in vowels
                w_start+=1
        return ans

#Submission 1 - 224 ms
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        ans=0
        i=0
        j=0
        cur_ans=0
        while j<len(s):
            if s[j] in vowels:
                cur_ans+=1 
            if j-i+1==k:
                ans=max(cur_ans,ans)
                if s[i] in vowels:
                    cur_ans-=1
                i+=1
            j+=1
        return ans