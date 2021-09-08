# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l=0
        h=head
        ans=head
        while head:
            l+=1
            head=head.next
        if l==1:
            return None
        if l==n:
            return ans.next
        prev=None
        l=l-n
        a=0
        while a<l:
            prev=h
            h=h.next
            a+=1
        h=h.next
        prev.next=h
        return ans