# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to seamlessly handle edge cases 
        # (like removing the very first head node)
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # 1. Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # 2. Move both pointers together until fast reaches the last node
        # The gap between slow and fast will stay exactly n nodes apart
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # 3. slow.next is now the node to delete. 
        # We skip it by changing slow's pointer to slow.next.next
        slow.next = slow.next.next
        
        # Return the actual head of the modified list
        return dummy.next
