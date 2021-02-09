class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans=[]
        if x>1 and y>1:
            for i in range(int(log(bound,x))+1):
                for j in range(int(log(bound,y))+1):
                    a=(x**i)+(y**j)
                    if a<=bound:
                        if a not in ans:
                            ans.append(a)
                    else:
                        break
        elif x==1 and y==1:
            if bound>1:
                ans.append(2)
        elif x==1:
            for j in range(int(log(bound,y))+1):
                a=1+(y**j)
                if a<=bound:
                    if a not in ans:
                        ans.append(a)
                else:
                    break
        elif y==1:
            for i in range(int(log(bound,x))+1):
                a=1+(x**i)
                if a<=bound:
                    if a not in ans:
                        ans.append(a)
                else:
                    break
        else:           
            for i in range(bound):
                for j in range(bound):
                    a=(x**i)+(y**j)
                    if a<=bound:
                        if a not in ans:
                            ans.append(a)
                    else:
                        break
        return ans