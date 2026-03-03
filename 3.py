def lengthOfLongestSubstring(self, s: str) # defining the function 
        left = 0
        seen = set()
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
    # to use this code in vs code you can directly do ctrl-c to ctrl-v 


