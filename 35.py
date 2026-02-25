nums = [1, 3, 6]
target = 7
i = 0
b = len(nums)
for i in range(len(nums)):
    if nums[i] == target:
        print(i)
        break

    elif nums[i] > target:
        nums.insert(i, target)
        print(i)
        break
    elif nums[b-1] < target:
        nums.insert(b,target)
        print(b)
        break
    else:
       i = i+1