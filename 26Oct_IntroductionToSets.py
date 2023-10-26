#
# https://www.hackerrank.com/challenges/python-lists/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
#
# Task
# Now, let's use our knowledge of sets and help Mickey. Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student 
# Mickey to compute the average of all the plants with distinct heights in her greenhouse.
#
# Function Description
# Complete the average function in the editor below.
# average has the following parameters:
# int arr: an array of integers
#
# Returns
# float: the resulting float value rounded to 3 places after the decimal
#
# Input Format
# The first line contains the integer, , the size of .
# The second line contains the  space-separated integers, .
#
# Sample Input
# STDIN                                       Function
# -----                                       --------
# 10                                          arr[] size N = 10
# 161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
#
# Sample Output
# 169.375
#
# Explanation
# Here, set is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.
#
def average(array):
    set_array = set(array)
    sum_array = sum(set_array)
    result = round((sum_array/len(set_array)), 3)  
    return result
