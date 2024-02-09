#!/usr/bin/python3

"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
"""


class Solution(object):

    def two_sum(self, nums, target):
        """
        	:type nums: List[int]
        	:type target: int
        	:rtype: List[int]
        """

        # Storing the complement of each number and its index
        number_dict = {}

        for i, num in enumerate(nums):
			# Calculate the complement (target - current number)
            complement = target - num

			# Checking if the complement is already in the dictionary
            if complement in number_dict:
                return [number_dict[complement], i]

			# Adds the current number and its index to the dictionary if not found
            number_dict[num] = 1

        return []