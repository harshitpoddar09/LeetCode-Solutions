#SUBMISSION 2 - 32ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tortoise=head
        hare=head
        while hare and hare.next:
            tortoise=tortoise.next
            hare=hare.next.next
        return tortoise

#SUBMISSION 1 - 24ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l=0
        h=head
        while head:
            l+=1
            head=head.next
        c=0
        while c<l//2:
            h=h.next
            c+=1
        return h