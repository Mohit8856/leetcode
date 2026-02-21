# to run this code in vs code just copy it and call the function 
# to use this code in leet code diretly you just do ctrl-c to ctrl-v
def plusOne(self, digits):
    
        n = len(digits)

       
       
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

       
       

        return [1] + digits    
