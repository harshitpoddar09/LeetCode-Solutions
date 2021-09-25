class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==0:
            return []
        def letter(digits):
            if len(digits)==0:
                return ['']
            char=digits[0]
            rem_digits=digits[1:]
            rres=letter(rem_digits)
            mres=[]
            for i in d[char]:
                for j in rres:
                    mres.append(i+j)
            return mres
        return letter(digits)