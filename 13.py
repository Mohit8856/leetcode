class Solution:
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]

        return ans


# Test Cases
obj = Solution()

print(obj.romanToInt("III"))      # Expected: 3
print(obj.romanToInt("LVIII"))    # Expected: 58
print(obj.romanToInt("MCMXCIV"))  # Expected: 1994
print(obj.romanToInt("IV"))       # Expected: 4
print(obj.romanToInt("IX"))       # Expected: 9
print(obj.romanToInt("XL"))       # Expected: 40
print(obj.romanToInt("XC"))       # Expected: 90
print(obj.romanToInt("CD"))       # Expected: 400
print(obj.romanToInt("CM"))       # Expected: 900
print(obj.romanToInt("MMXXVI"))   # Expected: 2026