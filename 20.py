class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Hash map to instantly look up the matching opening bracket for a closing bracket
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if it's not empty; otherwise, use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the popped element, the string is invalid
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return not stack
