class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.')==3:
            ip=IP.split('.')
        elif IP.count(':')==7:
            ip=IP.split(':')
        else:
            return 'Neither'
        n=len(ip)
        if n==4:
            for i in ip:
                if len(i)==0 or len(i)>3:
                    return 'Neither'
                if (i[0]=='0' and len(i)!=1) or not i.isdigit() or int(i)>255:
                    return 'Neither'
            return 'IPv4'
        else:
            allowed='0123456789abcdefABCDEF'
            for i in ip:
                if len(i)==0 or len(i)>4 or not all(j in allowed for j in i):
                    return 'Neither'
            return 'IPv6'