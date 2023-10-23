#
# https://www.hackerrank.com/challenges/collections-counter/problem
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
from collections import Counter

if __name__ == '__main__':
    no_shoes = (input())
    shoe_sizes = input()
    no_customers = input()
    cust_db = []
    total_profit = 0
    for i in range(int(no_customers)):
        temp = input()
        work = temp.split(' ')
        cust_db.append([int(a) for a in work])
    shoes_sizes_db = Counter([int(b) for b in shoe_sizes.split(' ')])

    for value in cust_db:
        if shoes_sizes_db[value[0]] > 0:
            total_profit += value[1]
            shoes_sizes_db[value[0]] -= 1
    print(total_profit)
#
#####################################################################################################################################################
#
from collections import Counter

if __name__ == "__main__":
    _ = input()  # placeholder for input value as no_shoes isn't used
    shoe_sizes = map(int, input().split()) # split shoe sizes into list then map into ints
    no_customers = int(input()) # number of customers
    shoe_sizes_db = Counter(shoe_sizes) # use the Counter class to create a dictionary of shoe sizes
    total_profit = 0 # initialise total profit

    for _ in range(no_customers): # iterate through each customer (based on no_customers)
        size, price_paid = map(int, input().split()) # split the input [size, price_paid] into list then map into ints
        if shoe_sizes_db[size] > 0: # if the size is in stock (not 0 in the dictionary)
            total_profit += price_paid # add the price_paid to total_profit
            shoe_sizes_db[size] -= 1 # reduce the stock by 1

    print(total_profit) # print the total profit
