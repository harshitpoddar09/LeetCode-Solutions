#Submission 2 - 17.5 mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        slow=head
        fast=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False

#Submission 1 - 18.2 mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a=set()
        while head:
            if a and head in a:
                return True
            else:
                a.add(head)
            head=head.next
        return False