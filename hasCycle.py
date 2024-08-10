# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        temp=head
        if head is None or head.next is None:
            return False
        fast=head.next
        while (fast.next) and (fast.next).next :
            if temp==fast:
                return True
            temp=temp.next
            fast=(fast.next).next
        return False
        