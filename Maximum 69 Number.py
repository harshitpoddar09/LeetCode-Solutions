class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=list(str(num))
        if ans.count('6')==0:
            return num
        for i in range(len(ans)):
            if ans[i]=='6':
                ans[i]='9'
                break
        return ''.join(ans)