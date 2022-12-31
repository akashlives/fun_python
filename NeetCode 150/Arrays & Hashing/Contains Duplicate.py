# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check whether list of numbers contains duplicate numbers
        Args:
            nums List: List of Numbers

        Returns: Boolean True or False
        """
        if len(nums) > len(set(nums)):
            return True
        else:
            return False

    def containsDuplicateAnotherOne(self, nums: List[int]) -> bool:
        """
        Check whether list of numbers contains duplicate numbers
        Args:
            nums List: List of Numbers

        Returns: Boolean True or False
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
