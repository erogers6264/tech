# stock_prices_yesterday, Ethan Rogers & Leon Cervantes
# Description: An program for determining the best
# profit possible from 1 purchase and 1 sale of Apple
# stock yesterday.


stock_prices_yesterday = [10, 7, 5, 4, 2, 1]


def get_max_profit(stock_prices_yesterday):
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    lowest_so_far = stock_prices_yesterday[0]
    # go through every time
    for index, price in enumerate(stock_prices_yesterday):
            if index == 0:
                continue
            potential_profit = price - lowest_so_far
            # New max profit is higher of the two
            max_profit = max(potential_profit, max_profit)
            lowest_so_far = min(lowest_so_far, price)
    return max_profit

print(get_max_profit(stock_prices_yesterday))