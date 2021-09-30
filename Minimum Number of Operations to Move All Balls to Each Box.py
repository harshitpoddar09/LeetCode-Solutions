class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        idx=[]
        for i in range(len(boxes)):
            if boxes[i]=='1':
                idx.append(i)
        for i in range(len(boxes)):
            ans.append(sum(abs(j-i) for j in idx))
        return ans