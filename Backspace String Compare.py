class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_list=[]
        t_list=[]
        for i in S:
            s_list.append(i)
        for j in T:
            t_list.append(j)
        p=0
        while p<len(s_list):    
            if s_list[p]=='#':
                s_list.pop(p)
                if p-1>=0:
                    s_list.pop(p-1)
                    p=p-1
            else:
                p+=1
        q=0
        while q<len(t_list):    
            if t_list[q]=='#':
                t_list.pop(q)
                if q-1>=0:
                    t_list.pop(q-1)
                    q=q-1
            else:
                q+=1
        s=''.join(s_list)
        t=''.join(t_list)
        return s==t