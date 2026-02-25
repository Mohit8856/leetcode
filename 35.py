nums = [1, 3, 6] # testing list , you can change it
target = 7 # testing target , you can change it 
b = len(nums)
i = 0 # initialization
for i in range(len(nums)):  # for loop till len of elements in nums
    if nums[i] == target: # condition when element is already there in the list 
        print(i) # then print the index . While you use this code in leetcode change it to return
        break # no further exicution of the code 

    elif nums[i] > target: # when the target is found in mid of the list
        nums.insert(i, target)
        print(i)
        break
    elif nums[b-1] < target:
        nums.insert(b,target)
        print(b)
        break
    else:

       i = i+1
