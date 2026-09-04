class Solution(object):
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []

        for value, symbol in zip(values, symbols):
            count = num // value
            if count:
                result.append(symbol * count)
                num %= value

        return "".join(result)
        # this code is written with using for loop , it may be done with some other meathods , its tome complexity is - 2mlS
