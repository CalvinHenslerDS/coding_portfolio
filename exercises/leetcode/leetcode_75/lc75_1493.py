'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        counter = 0
        max_length = 0

        while right < len(nums):
            if nums[right] == 0:
                counter += 1
            
            while counter > 1:
                if nums[left] == 0:
                    counter -= 1
                left += 1
            
            right += 1

            if right - left > max_length: max_length = right - left

        if max_length == 0: return max_length
        else: return max_length - 1
                
sol = Solution()

print(sol.longestSubarray([1,1,0,1]))
print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(sol.longestSubarray([1,1,1]))