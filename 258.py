def sum_of_digits(num):
   while num > 10:# cheacking if the number is greater than 10 or not which is gernally means that the number is single digit or not
    num = sum(int(i) for i in str(num))# it is a combination of a loop and a generator expression that calculates the sum of the digits of the number.
   return num# after performing the sum of the digits, it returns the final result which is a single digit number.
   
# above code is perfect in space complexity but not sufficient in time complexity   