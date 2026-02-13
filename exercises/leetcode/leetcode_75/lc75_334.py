'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = float('inf')
        second_smallest = float('inf')

        for number in nums:
            if number < smallest:
                smallest = number
            elif number < second_smallest:
                second_smallest = number
            else:
                if number > second_smallest:
                    return True
        return False


sol = Solution()
print(sol.increasingTriplet([1,2,3,4,5]))
print(sol.increasingTriplet([5,4,3,2,1]))
print(sol.increasingTriplet([2,1,5,0,4,6]))