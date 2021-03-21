class Solution:
    def secondHighest(self, s: str) -> int:
        digits=['1','2','3','4','5','6','7','8','9','0']
        alpha=[]
        for i in s:
            if i in digits:
                alpha.append(int(i))
        alpha=list(set(alpha))
        alpha.sort(reverse=True)
        if len(alpha)>1:
            return alpha[1]
        return -1