class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record=[]
        j=-1
        for i in ops:
            if i=='C':
                record.pop()
                j-=1
            elif i=='D':
                record.append(2*record[j])
                j+=1
            elif i=='+':
                record.append(record[j]+record[j-1])
                j+=1
            else:
                record.append(int(i))
                j+=1
        return sum(record)