# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        while head:
            nodes.append(head.val)
            head=head.next
        nodes.sort()
        h=ListNode(nodes[0])
        ans=h
        for i in range(1,len(nodes)):
            h.next=ListNode(nodes[i])
            h=h.next
        return ans