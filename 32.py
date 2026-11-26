class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = max_len = 0
        
        # Left-to-right scan
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                if 2 * right > max_len:
                    max_len = 2 * right
            elif right > left:
                left = right = 0
                
        left = right = 0
        
        # Right-to-left scan
        for ch in reversed(s):
            if ch == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                if 2 * left > max_len:
                    max_len = 2 * left
            elif left > right:
                left = right = 0
                
        return max_len
