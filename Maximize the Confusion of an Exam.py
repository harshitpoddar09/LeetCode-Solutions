class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=1
        w1_start=0
        max_T=0
        for w1_end in range(len(answerKey)):
            if answerKey[w1_end]=='T':
                max_T+=1
            if w1_end-w1_start+1-max_T>k:
                if answerKey[w1_start]=='T':
                    max_T-=1
                w1_start+=1
            ans=max(ans,w1_end-w1_start+1)
        w2_start=0
        max_F=0
        for w2_end in range(len(answerKey)):
            if answerKey[w2_end]=='F':
                max_F+=1
            if w2_end-w2_start+1-max_F>k:
                if answerKey[w2_start]=='F':
                    max_F-=1
                w2_start+=1
            ans=max(ans,w2_end-w2_start+1)
        return ans