#
# https://www.hackerrank.com/challenges/capitalize/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
#
# Input Format
# A single line of input containing the full name, S.
#
# Constraints
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
#
# Output Format
# Print the capitalized string, S.
#
# Sample Input
# chris alan
#
# Sample Output
# Chris Alan
#
import re
def solve(name):
    # print('initial name', name)
    name = re.split(r'(\s)', name)
    # print('after re.split name', name)
    # print('filter(lambda x: x != "", name), filter(lambda x: x != "", name)')
    name = list(filter(lambda x: x != "", name))
    # print(name)
    res = []
    for i in name:
        temp = list(i)
        if temp[0].isalpha() and temp[0] != " ":
            temp[0] = temp[0].upper()
        res.append("".join(temp))
    return "".join(res)
#
#####################################################################################################################################################
#
import re

def solve(name):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
