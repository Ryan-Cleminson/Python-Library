# Min Combinations
# Problem Description
# Alexander The great, while roaming the stretch of Turkey, came across a wise man.

# He asked the wise man, "Who is the greatest conqueror of all?". The wise man replied, "A person with great strength and intelligence. Whosoever can solve my puzzle will go on to become the greatest!". The puzzle is as follows; Given two integers 'n1' and 'n2', select two integers 'a' and 'b', such as to solve the equation (n1 * a + n2 * b = x). But there is a catch, 'x' is the smallest positive integer which satisfies the equation. Can you help Alexander become the greatest?

# Constraints
# 1 <= T <= 1000

# -10^7 <= a, b <= 10^7

# 0 <= n1, n2 <= 10^7

# Input Format
# The first line contains the number of Test cases T.

# Next T lines contains two space-separated integers, n1 and n2.

# Output
# Print the value of x.

# Test Case

# Explanation
# Example 1

# Input

# 1

# 34818 45632

# Output

# 2

# Explanation

# Given n1 = 34818 and n2 = 45632, if we choose a = 3553 and b = -2711, we get

# => n1 * a + n2 * b = x

# => 34818 * 3553 + 45632 * (-2711)

# => 2

# Note: No other value of a and b, within the range, will give smaller value than 2.

import math

def chooseAB(n1,n2):
    
    # a must be greater than or equal to -10000000
    # b must be lesser than or equal to 10000000
    a = 0
    b = 0
    X = 10000000

    for a in range(10000000,-10000000,-1):
        
        for b in range(-10000000,10000000, 1):
            Temp = int((n1*a) + (n2*b))
            if Temp < X and Temp > 0:
                X = int(Temp)
                return X
    else:
        print("Problem")


# (n1 * a + n2 * b = x)

print ("Input\n")
Test_Cases = 0
n1 = -1
n2 = -1

while int(Test_Cases) < 1 or int(Test_Cases) > 1000:
    print("Test Cases: ")
    Test_Cases = input()



# while n1 < 0 or n2 > 10^7:
#     # n1 has to be greater than or equal to 0 
#     # n2 must be lesser than or equal to 10000000
#     print ("N1: ")
#     n1 = int(input())
#     print(n1)
#     print ("N2: ")
#     n2 = int(input())
#     print(n2)
n1 = int(input())
n2 = int(input())

X = chooseAB(n1,n2)

print("Output\n")

print(X)
