def mySqrt(x: int) -> int:
    """
    Returns the integer square root of a non-negative integer x.
    The integer square root is the greatest integer r such that r*r <= x.
    """

    # Base cases:
    # If x is 0 or 1, the square root is the number itself
    if x == 0 or x == 1:
        return x

    # Initialize binary search boundaries
    left = 1
    right = x
    answer = 0  # To store the last valid mid value

    # Binary search loop
    while left <= right:
        mid = (left + right) // 2

        # If mid^2 equals x, we found the exact square root
        if mid * mid == x:
            return mid

        # If mid^2 is less than x, mid is a valid candidate
        elif mid * mid < x:
            answer = mid
            left = mid + 1

        # If mid^2 is greater than x, discard right half
        else:
            right = mid - 1

    # Return the largest integer whose square is <= x
    return answer