# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        curr=head
        fast=head
        while (fast.next)!=None:
            curr=curr.next
            if (fast.next).next:
                fast=(fast.next).next
            else:
                return curr
        return curr

                
            
        
        
        
            
        