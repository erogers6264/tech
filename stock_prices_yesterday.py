# stock_prices_yesterday, Ethan Rogers & Leon Cervantes
# Description: An program for determining the best
# profit possible from 1 purchase and 1 sale of Apple
# stock yesterday.


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]


def get_max_profit(stock_prices_yesterday):
    max_profit = 0
    lowest_so_far = stock_prices_yesterday[0]
    # go through every time
    for price in stock_prices_yesterday:
            lowest_so_far = min(lowest_so_far, price)
            potential_profit = price - lowest_so_far
            # New max profit is higher of the two
            max_profit = max(potential_profit, max_profit)
    return max_profit

print(get_max_profit(stock_prices_yesterday))