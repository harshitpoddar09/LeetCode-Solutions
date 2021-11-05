# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes=[]
        for head in lists:
            while head:
                nodes.append(head.val)
                head=head.next
        nodes.sort()
        if not nodes:
            return None
        cur=ListNode(nodes[0])
        ans=cur
        for i in range(1,len(nodes)):
            cur.next=ListNode(nodes[i])
            cur=cur.next
        return ans