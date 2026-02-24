n = 27 # taking a sample value for this code 
i = 0 # initialization 

while 3**i <= n: #condition
    if 3**i == n: # cheacking for true condition 
        print("True")
        break # break this block  of code 
    else:
        i += 1 # update the value of i to cheack further
else: # if above condition in while loop will  satisfy then  it will five , print or return false as default   but if condition  inside the while loop is satisfy then it break and no exsicution take place

    print("False")

# to use this code in vs code you can directly do ctrl-c to ctrl-v  but if you want it on leetcode then replace print with return and remove n = 27
