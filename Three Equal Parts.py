class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones=0
        idx_1=[]
        for i in range(len(arr)):
            if arr[i]==1:
                ones+=1
                idx_1.append(i)
                arr[i]='1'
            else:
                arr[i]='0'
        if ones%3!=0:
            return [-1,-1]
        if ones==0:
            return [0,2]
        n=ones//3
        z=len(arr)-1-idx_1[-1]
        a=idx_1[0]
        b=idx_1[n-1]
        c=idx_1[n]
        d=idx_1[2*n-1]
        e=idx_1[2*n]
        f=idx_1[-1]
        if c-b<=z or e-d<=z:
            return [-1,-1]
        part1=arr[:b+z+1]
        part2=arr[b+z+1:d+z+1]
        part3=arr[d+z+1:]
        bin1=int(''.join(part1),2)
        bin2=int(''.join(part2),2)
        bin3=int(''.join(part3),2)
        if bin1==bin2 and bin2==bin3:
            return [b+z,d+z+1]
        return [-1,-1]