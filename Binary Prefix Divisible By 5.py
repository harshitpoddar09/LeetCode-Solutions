#Submission 2 - 316 ms
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        dec=0
        ans=[]
        for i in range(len(A)):
            dec=(dec*2)+A[i]
            if dec%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans

#Submission 1 - 932 ms
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        binary=''
        dec=0
        ans=[]
        for i in range(len(A)):
            binary+=str(A[i])
            dec=int(binary,2)
            if dec%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans