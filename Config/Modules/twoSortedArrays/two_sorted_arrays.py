#!/usr/bin/python3

"""
A function that finds the median of two sorted arrays
"""


def median_array(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (x + y + 1) // 2 - partition_x

        max_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        max_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]

        min_x = float('inf') if partition_x == x else nums1[partition_x]
        min_y = float('inf') if partition_y == y else nums2[partition_y]

        if max_x <= min_y and max_y <= min_x:
            if (x + y) % 2 == 0:
                return (max(max_x, max_y) + min(min_x, min_y)) / 2.0
            else:
                return max(max_x, max_y)
        elif max_x > min_y:
            high = partition_x - 1
        else:
            low = partition_x + 1
