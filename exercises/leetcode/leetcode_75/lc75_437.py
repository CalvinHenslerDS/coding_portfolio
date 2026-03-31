'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.


Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
'''
from collections import defaultdict
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            count = prefix_sums[current_sum - targetSum]
            prefix_sums[current_sum] += 1
            
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            prefix_sums[current_sum] -= 1
            
            return count

        return dfs(root, 0)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr: return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    sol = Solution()
    test_tree = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    result = sol.pathSum(test_tree, 8)
    print(f"Paths summing to 8: {result}")