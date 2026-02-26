left = 1
right = 22
lst = []

for i in range(left, right + 1):
    if i <= 10:
        lst.append(i)
    else:
        a = str(i)
        valid = True   

        for j in a:
            k = int(j)

            if k == 0 or i % k != 0:
                valid = False
                break

        if valid:
            lst.append(i)

print(lst)
