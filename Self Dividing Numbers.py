class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfdiv(a):
            for i in a:
                if i=='0':
                    return False
                elif int(a)%int(i)!=0:
                    return False
            return True
        ans=[]
        for i in range(left,right+1):
            a=str(i)
            if selfdiv(a):
                ans.append(int(a))
        return ans