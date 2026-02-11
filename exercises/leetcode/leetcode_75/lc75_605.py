'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        n_allowed = 0

        permitted_plants = [True] * len(flowerbed)
        for index, pot in enumerate(flowerbed):
            if index == 0:
                if pot == 1:
                    permitted_plants[index] = permitted_plants[index+1] = False
            if index == len(flowerbed):
                if pot == 1:
                    permitted_plants[index-1] = permitted_plants[index] = permitted_plants[index+1] = False
            else:
                if pot == 1:
                    permitted_plants[index-1] = permitted_plants[index] = False
        
        for element in permitted_plants:
            if element == True:
                n_allowed += 1

        if n_allowed >= n:
            return True
        else:
            return False

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1],1))
print(sol.canPlaceFlowers([1,0,0,0,1],2))