# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
       
        # Create a dummy node to act as the starting anchor
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists until one runs out
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the pointer forward in the merged list
            current = current.next
            
        # Append the remaining nodes of whichever list is left over
        current.next = list1 if list1 else list2
        
        # The actual head of the merged list is the next node after dummy
        return dummy.next
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        