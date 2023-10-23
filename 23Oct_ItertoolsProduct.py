#
# https://www.hackerrank.com/challenges/itertools-product/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
from itertools import product

if __name__ == '__main__':
    line1 = line2 = []
    line1 = [int(x) for x in input().split(' ')]
    line2 = [int(y) for y in input().split(' ')]
    result = []
    
    output = list(product(line1, line2))
    print (' '.join(str(x) for x in output))
#
#####################################################################################################################################################
#
from itertools import product

if __name__ == '__main__':
    line1 = line2 = []
    line1 = [int(x) for x in input().split(' ')]
    line2 = [int(y) for y in input().split(' ')]
    result = []
    
    output = list(product(line1, line2))
    for x in output:
        print(''.join(str(x)), end=' ')
