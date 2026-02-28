divident = 7
divisor = -3
class Solution(object):
    def divide(self, dividend, divisor):

        # Handle division by zero
        if divisor == 0:
            return 0

        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)

        # Convert to +tive 
        c = abs(dividend)
        d = abs(divisor)

        n = 0

        # Subtract until smaller
        while c >= d:
            c = c - d
            n += 1

        # Apply sign
        if negative:
            return -n
        else:
            return n