# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head=list1
        count=0
        while count!=a:
            prev=head
            head=head.next
            count+=1
        while count!=b:
            head=head.next
            count+=1
        prev.next=list2
        while list2.next:
            list2=list2.next
        list2.next=head.next
        return list1