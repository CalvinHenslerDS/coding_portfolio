'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        read = len(nums) - 1

        for num in nums[::-1]:
            
            if num == 0:
                del nums[read]
                nums.append(0)
            
            read -= 1

        return nums




sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))
print(sol.moveZeroes([0]))

# Alternative solution using two-pointer swap (to avoid del bottleneck):

class Solution(object):
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        last_nonzero = 0

        for num in range(len(nums)):
            if nums[num] != 0:
                nums[last_nonzero], nums[num] = nums[num], nums[last_nonzero]
                last_nonzero += 1

        return nums
