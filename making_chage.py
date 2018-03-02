# Your quirky boss collects rare, old coins...

# They found out you're a programmer and asked you to solve something they've been wondering for a long time.

# Write a function that, given:

# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.

# Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢), your program would output 4—the number of ways to make 4¢ with those denominations:

# 1. 1¢, 1¢, 1¢, 1¢
# 2. 1¢, 1¢, 2¢
# 3. 1¢, 3¢
# 4. 2¢, 2¢

def change_possibilities_top_down(amount_left, denominations, current_index=0):
    # Base cases:
    # We hit the amount spot on. yes!
    if amount_left == 0:
        return 1
        
    # We overshot the amount left (used too many coins)
    if amount_left < 0:
        return 0
        
    # We're out of denominations
    if current_index == len(denominations):
        return 0
        
    print "checking ways to make %i with %s" % (
        amount_left,
        denominations[current_index:],
    )
    
    # Choose a current coin
    current_coin = denominations[current_index]
    
    # See how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(
            amount_left,
            denominations,
            current_index + 1,
        )
        amount_left -= current_coin
        
    return num_possibilities
    
