#!/usr/bin/env python
# -*- coding: utf-8 -*-

# find_dup.py

# We have a list of integers, where:

#   1. The integers are in the range 1..n
#   2. The list has a length n + 1

# It follows that our list has at least one integer which appears at least twice.
# But it may have several duplicates, and each duplicate may appear more than twice.

# Write a function which finds an integer that appears more than once in our list.
# (If there are multiple duplicates, you only need to find one of them.)

# We're going to run this function on our new, super-hip MacBook Pro With Retina Display™.
# Thing is, the damn thing came with the RAM soldered right to the motherboard, so we
# can't upgrade our RAM. So we need to optimize for space!

list_of_integers = [1, 2, 3, 4, 4, 4, 7, 8, 9, 2]

def find_dup(list_of_integers):
	# Create a set which is all the unique integers
	set_of_integers = set(list_of_integers)
	# For each of those, check if the count of the integer in the original list is greater than one
	for i in set_of_integers:
		# That means it's a duplicate so return it and we're done
		if list_of_integers.count(i) > 1:
			return i
	# No duplicates were found
	return -1

print find_dup(list_of_integers)