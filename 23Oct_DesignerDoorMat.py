#
# https://www.hackerrank.com/challenges/designer-door-mat/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
if __name__ == '__main__':
    line = []
    line = [int(x) for x in input().split(' ')]
    
    center_line = 'WELCOME'.center(line[1], '-')
        
    pattern = '.|.'

    for row in range(1, (int((line[0]-1) / 2)) + 1):
        pattern_line = (pattern*(row*2 - 1)).center(line[1], '-')
        print(pattern_line)
    
    print(center_line)
    
    for row in range((int((line[0]) / 2)), 0, -1):
        pattern_line = (pattern*(row*2 - 1)).center(line[1], '-')
        print(pattern_line)
