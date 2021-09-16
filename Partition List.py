#SUBMISSION 2 - 36ms 14.1mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less=ListNode(0)
        less1=less
        more=ListNode(0)
        more1=more
        while head:
            if head.val<x:
                less.next=head
                less=less.next
            else:
                more.next=head
                more=more.next
            head=head.next
        more.next=None
        less.next=more1.next
        return less1.next

#SUBMISSION 1 - 32ms 14.3mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less=[]
        more=[]
        while head:
            if head.val<x:
                less.append(head.val)
            else:
                more.append(head.val)
            head=head.next
        dummy=ListNode(0)
        ans=dummy
        for i in less:
            dummy.next=ListNode(i)
            dummy=dummy.next
        for j in more:
            dummy.next=ListNode(j)
            dummy=dummy.next
        return ans.next