class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            # Skip duplicate first elements (optional optimization)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Perfect match
                if current == target:
                    return current

                # Move pointers
                elif current < target:
                    left += 1
                else:
                    right -= 1

        return closest
test_cases = [
    ([-1, 2, 1, -4], 1),
    ([0, 0, 0], 1),
    ([1, 2, 3, 4], 6),
    ([-8, -6, -5, -2], -10),
    ([-5, -2, 0, 3, 8], 4),
    ([1, 1, 1, 0], -100),
    ([5, 2, 7, 9, 1], 100),
    ([5, 2, 7, 9, 1], -100),
    ([3, -2, 1], 5),
    ([4, -1, -4, 2, 6], 3),
]

obj = Solution()

for nums, target in test_cases:
    print(f"nums = {nums}")
    print(f"target = {target}")
    print("closest sum =", obj.threeSumClosest(nums, target))
    print("-" * 40)    