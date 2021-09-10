# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        l=0
        h=head
        while head.next:
            l+=1
            head=head.next
        l+=1
        if l==1:
            return h
        head.next=h
        k=k%l
        c=1
        while c<l-k:
            h=h.next
            c+=1
        ans=h.next
        h.next=None
        return ans