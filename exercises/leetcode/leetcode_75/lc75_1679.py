'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''

# Expensive solution

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left_pointer = 0
        right_pointer = 1
        counter = 0

        while left_pointer < len(nums) - 1:
            if nums[left_pointer] + nums[right_pointer] == k:
                del nums[right_pointer], nums[left_pointer]
                counter += 1
                left_pointer = 0
                right_pointer = 1
                continue
            if right_pointer < len(nums) - 1:
                right_pointer += 1
            else:
                left_pointer += 1
                right_pointer = left_pointer + 1
        
        return counter

sol = Solution()
print(sol.maxOperations([1,2,3,4], 5))
print(sol.maxOperations([3,1,3,4,3], 6))

# Two-Pointer Solution (O(nlog(n)))

class Solution2(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(nums) - 1
        counter = 0

        nums.sort()

        while left_pointer < right_pointer:
            current_sum = nums[left_pointer] + nums[right_pointer]
            if current_sum == k:
                counter += 1
                left_pointer += 1
                right_pointer -= 1
            elif current_sum < k:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return counter

sol = Solution2()
print(sol.maxOperations([1,2,3,4], 5))
print(sol.maxOperations([3,1,3,4,3], 6))

# Hash Map Solution (O(n))

from collections import Counter

class Solution3(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count_dictionary = Counter(nums)
        counter = 0

        for item in list(count_dictionary.keys()):
            target = k - item

            if target in count_dictionary:
                if item == target:
                    counter += count_dictionary[item] // 2
                elif target > item:
                    pairs = min(count_dictionary[item], count_dictionary[target])
                    counter += pairs
        
        return counter

sol = Solution3()
print(sol.maxOperations([1,2,3,4], 5))
print(sol.maxOperations([3,1,3,4,3], 6))