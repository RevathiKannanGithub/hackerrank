#
# https://www.hackerrank.com/challenges/python-lists/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
if __name__ == '__main__':
    N = int(input())
    output_arr = []
    
    for i in range(N):
        line = input().split(' ')
        if line[0] == 'insert':
            output_arr.insert(int(line[1]), int(line[2]))
        elif line[0] == 'print':
            print(output_arr)
        elif line[0] == 'remove':
            output_arr.remove(int(line[1]))
        elif line[0] == 'append':
            output_arr.append(int(line[1]))
        elif line[0] == 'sort':
            output_arr.sort()
        elif line[0] == 'pop':
            output_arr.pop()
        elif line[0] == 'reverse':
            output_arr = output_arr[::-1] 
        else:
            print('None')
