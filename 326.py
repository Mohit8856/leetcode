n = 27
i = 0

while 3**i <= n:
    if 3**i == n:
        print("True")
        break
    else:
        i += 1
else:
    print("False")