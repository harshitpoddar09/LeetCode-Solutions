#Submission 2 - 32 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=0
        while head:
            num=num*2+head.val
            head=head.next
        return num

#Submission 1 - 24 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=''
        while head:
            num+=str(head.val)
            head=head.next
        return int(num,2)