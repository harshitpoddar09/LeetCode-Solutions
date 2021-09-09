# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        a=set()
        ans=head
        prev=None
        while head and head.next:
            if head.val==head.next.val:
                a.add(head.val)
                while head and head.val in a:
                    head=head.next
                if prev==None:
                    ans=head
                else:
                    prev.next=head
                a.clear()
            else:
                prev=head
                head=head.next
        return ans