n = 27 # taking a sample value for this code 
i = 0 # initialization 

while 3**i <= n: #condition
    if 3**i == n: # cheacking for true condition 
        print("True")
        break # break this block  of code 
    else:
        i += 1 # update the value of i to cheack further
else: # if above condition in while loop will  satisfy then  it will five , print or return false as default  

    print("False")
