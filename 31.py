class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # 1. Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # 2. Binary search the descending suffix [i + 1, n - 1] for the rightmost element > nums[i]
        if i >= 0:
            left, right = i + 1, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 'right' lands on the rightmost index where nums[right] > nums[i]
            nums[i], nums[right] = nums[right], nums[i]
            
        # 3. Reverse the suffix in-place
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
