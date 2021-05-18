class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        for i in banned:
            paragraph=paragraph.replace(i,'')
        symbols="!?',;."
        for k in symbols:
            if k in paragraph:
                paragraph=paragraph.replace(k,' ')
        words=list(paragraph.split())
        ans=''
        c=0
        for j in set(words):
            if words.count(j)>c:
                c=words.count(j)
                ans=j
        return ans