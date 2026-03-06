# Find Median of Two Sorted Arrays (Python)

##1. Combine both input arrays `nums1` and `nums2` into a single list `num3`.
#2. Sort the combined list to maintain sorted order.
#3. Calculate the total number of elements `n`.
#4. Check whether the length `n` is **even or odd**:

  # * **If `n` is even:**
  #   The median is the average of the two middle elements.
   #* **If `n` is odd:**
   #  The median is the middle element of the sorted list.

## Python Implementation

#`python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        num3 = nums1 + nums2
        num3.sort()
        
        n = len(num3)
        
        if n % 2 == 0:
            c = n // 2
            d = c - 1
            return (num3[c] + num3[d]) / 2.0
        else:
            g = n // 2
            return num3[g]

## Example




## Time Complexity

#* Sorting the merged array takes **O((m+n) log(m+n))**

## Space Complexity

#* **O(m+n)** for storing the merged array.


#This approach is simple and easy to understand, although more optimized solutions exist using binary search with **O(log(min(m,n)))** time complexity.
