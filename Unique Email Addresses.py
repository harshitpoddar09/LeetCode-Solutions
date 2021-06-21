class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            a=emails[i].index('@')
            emails[i]=emails[i][:a].replace('.','')+emails[i][a:]
            a=emails[i].index('@')
            if '+' in emails[i][:a]:
                b=emails[i].index('+')
                emails[i]=emails[i][:b]+emails[i][a:]
        return len(set(emails))