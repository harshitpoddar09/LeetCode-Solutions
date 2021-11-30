class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table={}
        dishes=set()
        tables=set()
        for i in orders:
            no=int(i[1])
            dish=i[2]
            if no not in table:
                table[no]=[]
            table[no].append(dish)
            dishes.add(dish)
            tables.add(int(no))
        dishes=list(dishes)
        dishes=sorted(dishes)
        tables=list(tables)
        tables=sorted(tables)
        ans=[]
        ans.append(['Table']+dishes)
        for j in tables:
            data=[str(j)]+([0]*len(dishes))
            for k in range(len(dishes)):
                if dishes[k] in table[j]:
                    data[k+1]+=table[j].count(dishes[k])
            for i in range(len(data)):
                data[i]=str(data[i])
            ans.append(data)
        return ans