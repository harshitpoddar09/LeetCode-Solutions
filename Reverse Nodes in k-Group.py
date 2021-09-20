# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        length=0
        a=head
        while a:
            length+=1
            a=a.next
        groups=length//k
        extra=length%k
        if groups==0:
            return head
        prev=None
        count=0
        while groups:
            b=head
            if prev==None:
                while count<k:
                    new=head.next
                    head.next=prev
                    prev=head
                    head=new
                    count+=1
                    ans=prev
                count=0
            else:
                while count<k:
                    new=head.next
                    head.next=prev
                    prev=head
                    head=new
                    count+=1
                count=0
                tail.next=prev
            groups-=1
            tail=b
        if extra:
            tail.next=head
        else:
            tail.next=None
        return ans