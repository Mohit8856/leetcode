left = 1 # testing variable for the code . if you wnat to use this code directly on the leet code , remove it  before running in leetcode
right = 22 # testing variable for the code . if you wnat to use this code directly on the leet code , remove it  before running in leetcode
lst = []

for i in range(left, right + 1):
    if i <= 10:
        lst.append(i)
    else:
        a = str(i)
        valid = True  #  we use it to insure that the number is divisble by itself completly and also insure to not repeat the number in the list 

        for j in a:
            k = int(j)

            if k == 0 or i % k != 0:
                valid = False
                break

        if valid: 
            lst.append(i)

print(lst) # change print with return while using in leetcode 

