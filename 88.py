newnums1 = nums1[:m]
newnums2 = nums2[:n]

newnums = newnums1 + newnums2
newnums.sort()

nums1[:] = newnums  