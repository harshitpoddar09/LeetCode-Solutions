#Submission 2 - 724ms
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        seen=set()
        for i in trust:
            seen.add(i[0])
        if len(seen)!=n-1:
            return -1
        check=set()
        for j in range(1,n+1):
            if j not in seen:
                break
        for k in trust:
            if k[1]==j:
                check.add(k[0])
        if len(check)==n-1:
            return j
        return -1

#Submission 1 - 1191ms
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        d={}
        possible=[]
        for i in trust:
            if i[1] not in d:
                d[i[1]]=0
            d[i[1]]+=1
            if d[i[1]]==n-1:
                possible.append(i[1])
        for j in possible:
            for k in trust:
                if k[0]==j:
                    break
            else:
                return j
        return -1