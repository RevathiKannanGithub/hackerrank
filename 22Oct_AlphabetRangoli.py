#
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
a = 'abcdefghijklmnopqrstuvwxyz'

def print_rangoli(n):
    lines = []
    for i in range(0, n):
        order = '-'.join(a[i:n])
        reverse_order = order[::-1]
        print_ = reverse_order + order[1:]
        lines.append(print_)
    width = len(lines[0])
        
    for row in range(n-1, 0, -1):
        print(lines[row].center(width, '-'))
    
    for row in range(n):
        print(lines[row].center(width, '-'))
