#SUBMISSION 2 - 152ms 30.1mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr=[]
        new=head
        ans=new
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        for i in arr:
            new.val=i
            new=new.next
        return ans

#SUBMISSION 1 - 212ms 38mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        dummy=ListNode(0)
        ans=dummy
        for i in arr:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return ans.next