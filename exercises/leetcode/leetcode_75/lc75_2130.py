'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        fast_pointer = head
        slow_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        previous = None
        current = slow_pointer

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next 
            
        max_sum = float('-inf')

        left = head
        right = previous

        while right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next
        
        return max_sum
    
def build_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    sol = Solution()
    
    head1 = build_list([5, 4, 2, 1])
    result1 = sol.pairSum(head1)
    print(f"Test 1 Results: {result1}")

    head2 = build_list([4, 2, 2, 3])
    result2 = sol.pairSum(head2)
    print(f"Test 2 Results: {result2}")

    head3 = build_list([1, 100000])
    result3 = sol.pairSum(head3)
    print(f"Test 3 Results: {result3}")