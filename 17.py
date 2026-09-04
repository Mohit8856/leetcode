class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Return an empty list if the input string is empty
        if not digits:
            return []
            
        # Telephone keypad mapping using a standard dictionary
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Start with an empty string combination in our results list
        combinations = [""]
        
        # Process each digit one by one
        for digit in digits:
            next_combinations = []
            
            # Combine every existing string with each new possible letter
            for current_string in combinations:
                for letter in phone_map[digit]:
                    next_combinations.append(current_string + letter)
                    
            # Move to the next layer of combinations
            combinations = next_combinations
            
        return combinations
