#
# https://www.hackerrank.com/challenges/py-collections-deque/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
from collections import deque

if __name__ == '__main__':
    n = input()
    d = deque()
    
    for operation in range(int(n)):
        input_list = [x for x in input().split()]
        if input_list[0] == 'append':
            d.append(input_list[1])
        elif input_list[0] == 'appendleft':
            d.appendleft(input_list[1])
        elif input_list[0] == 'pop':
            d.pop()
        elif input_list[0] == 'popleft':
            d.popleft()
        elif input_list[0] == 'extend':
            d.extend(input_list[1])
        elif input_list[0] == 'extendleft':
            d.extendleft(input_list[1])
        elif input_list[0] == 'reverse':
            d.reverse()
        elif input_list[0] == 'rotate': 
            d.rotate(int(input_list[1]))   
        elif input_list[0] == 'remove':
            d.remove(input_list[1])
        elif input_list[0] == 'count':
            d.count(input_list[1])
        elif input_list[0] == 'clear':
            d.clear()
    print(' '.join(d))
