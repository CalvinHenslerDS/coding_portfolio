'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

# First solution, O(n^2) time complexity

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_height = 0
        right_height = 0
        width = 0
        max_area = 0

        for i in range(0, len(height)-1):
            for j in range(i+1, len(height)):
                height1 = height[i]
                height2 = height[j]
                lower_height = min(height1, height2)
                area = lower_height * (j - i)
                #print(index1, index2, index2-index1)
                if area > max_area: max_area = area

        return max_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))


class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left_index = 0
        right_index = len(height) - 1
        
        max_area = 0

        while left_index < right_index:
                height1 = height[left_index]
                height2 = height[right_index]
                lower_height = min(height1, height2)
                area = lower_height * (right_index - left_index)
                if area > max_area: max_area = area
                if height2 == lower_height: right_index -= 1
                else: left_index += 1

        return max_area

sol = Solution2()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))
