class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base Case: Valid combination found when string reaches length 2 * n
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Action 1: Add an opening parenthesis if we haven't used up all n
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Action 2: Add a closing parenthesis only if it won't exceed open ones
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        # Kick off the recursion starting with an empty string
        backtrack("", 0, 0)
        return result
