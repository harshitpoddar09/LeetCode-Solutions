#Submission 2 - 56ms
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=set()
        seen=set()
        w_seq=''
        for w_start in range(len(s)-9):
            w_seq=s[w_start:w_start+10]
            if w_seq in seen:
                ans.add(w_seq)
            else:
                seen.add(w_seq)
        return list(ans)

#Submission 1 - 68ms
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=set()
        seen=set()
        w_seq=''
        for w_end in range(len(s)):
            w_seq+=s[w_end]
            if w_end>=9:
                if w_seq in seen:
                    ans.add(w_seq)
                else:
                    seen.add(w_seq)
                w_seq=w_seq[1:]
        return list(ans)