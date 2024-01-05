# leetcode 2529. Maximum Count Of Positive Integer and Negative Integer
# Given an array 'nums' sorted in *non-decreasing order*, return the maximum
# between the number of positive integers and negative integers.
# 
# In other words, if the number of positive integers in nums is pos and the number of
# number of negative integers is neg, then return the maximum between pos and neg.
# 
# Solution in words:
# Get the number of negative numbers and positive numbers, remember 0 is not positive nor negative
# and then find which is higher, store that number in a variable (NOT storing positive or negative but storing
# the number of that type) e.g. if there are 4 negative numbers and 3 positive numbers, it will return 4 
#
# Links:
# Video: https://www.youtube.com/watch?v=U6I-Kwj-AvY
# Leetcode: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

# My code:

# Solution1:
# Create a negative_numbers and positve_numbers variable and 
# Find the amount of items in a given list, repeat x amount of times a check*
# 
def solution1(input_list):
    negative_numbers = 0
    positve_numbers = 0
    
    for i in range(len(input_list)):
        if input_list[i] > 0:
            positve_numbers += 1
        elif input_list[i] < 0:
            negative_numbers += 1

    return(max(negative_numbers, positve_numbers))

my_list1 = [-2,-1,-1,1,2,3]
my_list2 = [-3,2,1,0,0,1,2]
my_list3 = [5,20,66,1314]

print(f"my_list1 solution1 {solution1(my_list1)}")
print(f"my_list2 solution1 {solution1(my_list2)}")
print(f"my_list3 solution1 {solution1(my_list3)}")