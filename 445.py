class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        
        # Traverse first linked list
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        # Traverse second linked list
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        
        # Add from back using stacks
        while stack1 or stack2 or carry:
            total = carry
            
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
            
            carry = total // 10
            
            # Create new node
            node = ListNode(total % 10)
            node.next = head
            head = node
        
        return head