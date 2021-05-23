class Solution:
    def freqAlphabets(self, s: str) -> str:
        num=['1','2','3','4','5','6','7','8','9']
        char=['a','b','c','d','e','f','g','h','i']
        hash_num=['10#','11#','12#','13#','14#','15#','16#','17#','18#','19#','20#','21#','22#','23#','24#','25#','26#']
        hash_char=['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(17):
            s=s.replace(hash_num[i],hash_char[i])
        for j in range(9):
            s=s.replace(num[j],char[j])
        return s