class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        queue=[]
        zero=0
        one=0
        for i in s:
            if not queue:
                queue.append(i)
            else:
                if i==queue[-1]:
                    queue.append(i)
                else:
                    if queue[-1]=='0':
                        zero=max(zero,len(queue))
                    else:
                        one=max(one,len(queue))
                    queue=[]
                    queue.append(i)
        if queue[-1]=='0':
            zero=max(zero,len(queue))
        else:
            one=max(one,len(queue))
        return one>zero