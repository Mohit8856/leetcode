nums = [2,0,2,1,1,0]
r = 0
r_list = []
for i in nums:
    if i == 0:
        r += 1
        r_list.append(0)# cheacking for 0 and udateing the count of 0 and also appending 0 in the r_list
w = 0 
w_list = []    
for i in nums:
    if i == 1:
        w += 1   
        w_list.append(1)# cheacking for 1 and udateing the count of 1 and also appending 1 in the w_list    
b = 0 
b_list = []     
for i in nums:
    if i == 2:
        b += 1 
        b_list.append(2)# cheacking for 2 and udateing the count of 2 and also appending 2 in the b_list 
nums[:]= r_list + w_list + b_list # updating the original list nums by concatenating the r_list, w_list, and b_list. This effectively sorts the original list in-place, with all 0s followed by all 1s and then all 2s.
print(nums)       
