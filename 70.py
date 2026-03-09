n = int(input("enter the number of staires"))
if n <= 2:
            return n
        
        a, b = 1, 2
        
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        
        return b
       
