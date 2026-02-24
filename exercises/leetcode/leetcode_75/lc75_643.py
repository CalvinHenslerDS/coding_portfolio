'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value
and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

# Naive Sliding Window

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        left_pointer = 0
        right_pointer = k
        largest_total = float('-inf')

        while right_pointer <= len(nums):
            current_total = 0

            for index in range(left_pointer, right_pointer):
                print(nums[index])
                current_total += nums[index]
            if current_total > largest_total: largest_total = current_total
        
            left_pointer += 1
            right_pointer += 1

        largest_average = largest_total / k

        return largest_average
        

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
print(sol.findMaxAverage([5], 1))

# True Sliding Window

class Solution2(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        current_total = sum(nums[:k])
        largest_total = current_total

        for index in range(k, len(nums)):
            current_total += nums[index] - nums[index - k]
            if current_total > largest_total: largest_total = current_total

        largest_average = float(largest_total) / k

        return largest_average
    
sol = Solution2()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
print(sol.findMaxAverage([5], 1))