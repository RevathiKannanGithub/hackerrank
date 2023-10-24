#
# https://www.hackerrank.com/challenges/no-idea/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
if __name__ == '__main__':

    _ = input()
    array_ints = [int(x) for x in input().split(' ')]
    set1_ints = set([int(x) for x in input().split(' ')])
    set2_ints = set([int(x) for x in input().split(' ')])
  
    happiness = 0
    for i in array_ints:
        if i in set1_ints:
            happiness += 1    
        elif i in set2_ints:
            happiness -= 1
            
    print(happiness)
