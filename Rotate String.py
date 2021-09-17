#Submission 2 - 24ms 14.3mb
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and goal in s+s

#Submission 1 - 32ms 14.4mb
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)==0 and len(goal)==0:
            return True
        s=s+s
        cur_win=''
        for w_end in range(len(s)):
            cur_win+=s[w_end]
            if w_end+1>=len(s)//2:
                if cur_win==goal:
                    return True
                cur_win=cur_win[1:]
        return False