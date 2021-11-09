# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        h=head
        length=0
        while h:
            length+=1
            h=h.next
        q=length//k
        r=length%k
        ans=[]
        while k:
            cur=None
            prev=None
            if q:
                cur=head
                for i in range(q):
                    prev=head
                    head=head.next
            if r:
                if cur:
                    prev=head
                    head=head.next
                else:
                    cur=head
                    prev=head
                    head=head.next
                r-=1
            if prev:
                prev.next=None
            ans.append(cur)
            k-=1
        return ans