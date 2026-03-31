'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.


Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.


Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, max_so_far):
            if not node:
                return 0
            
            count = 0

            if node.val >= max_so_far:
                count = 1
                max_so_far = node.val
            
            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)
            
            return count

        return dfs(root, root.val)
    
from collections import deque

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

    root1 = build_tree([3, 1, 4, 3, None, 1, 5])
    print(f"Example 1 Good Nodes: {sol.goodNodes(root1)}")

    root2 = build_tree([3, 3, None, 4, 2])
    print(f"Example 2 Good Nodes: {sol.goodNodes(root2)}")