#---------------------------------------------------------------------
# LCM and HCFs from Coding Challenges (MEDIUM - solution)
# by Silvio Duka
#
# Last modified date: 2018-02-25
#
# LCM is the least common multiple of a set of numbers. 
# HCF is the highest common factor of a set of numbers. 
# 
# Consider 10 and 15: 
# Multiples of 10 are: 10, 20, 30, 40, ... 
# Multiples of 15 are: 15, 30, 45, 60, ... 
# => 30 is the LCM of 10 and 15. 
# 
# Factors of 10 are: 1, 2, 5, 10 
# Factors of 15 are: 1, 3, 5, 15 
# => 5 is the HCF of 10 and 15. 
#
# Tasks: 
# (Easy) Write a program to find the LCM and HCF of 2 numbers. 
# (Medium) Write a program to find the LCM and HCF of 3 numbers. 
# (Hard) Write a program to find the LCM and HCF of 4 or more numbers.
#---------------------------------------------------------------------

number1 = 10 # Insert a first number
number2 = 15 # Insert a second number
number3 = 20 # Insert a third number

def lcm(number1, number2, number3):

    number = number1 if number1 < number2 else (number2 if (number2 < number3) else number3)        

    for i in range(number, (number1 * number2 * number3) + 1, number):
        if (i % number1 + i % number2  + i % number3) == 0:
            return i
            
def hcf(number1, number2, number3):
    
    number = number1 if number1 < number2 else (number2 if (number2 < number3) else number3)  

    for i in range(number, 0, -1):
        if (number1 % i + number2 % i + number3 % i) == 0:
            return i

print("The LCM of [" + str(number1) + "," + str(number2) + "," + str(number3) + "] is " + str(lcm(number1, number2, number3)))
print("The HCF of [" + str(number1) + "," + str(number2) + "," + str(number3) + "] is " + str(hcf(number1, number2, number3)))