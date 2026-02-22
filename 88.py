# to run this code in vs code just change the last line to print and if you want to use it directly in leetcode so you can just ctrl-c to ctrl-v
newnums1 = nums1[:m] # indexing
newnums2 = nums2[:n] # indexing

newnums = newnums1 + newnums2 # addingf to indexed lists
newnums.sort() # sorting


nums1[:] = newnums  # updating nums1 not returning it as per the question
