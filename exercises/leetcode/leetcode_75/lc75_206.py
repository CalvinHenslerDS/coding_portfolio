'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:

Input: head = [1,2]
Output: [2,1]


Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
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

    # Iterative (O(1) Space Complexity)

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        previous_node = None
        current_node = head
        
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            
        return previous_node
    
    # Recursive (O(n) Space Complexity)

    def reverseList2(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head
        
        new_head = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
def build_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def list_to_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    sol = Solution()
    
    head1 = build_list([1, 2, 3, 4, 5])
    result1 = sol.reverseList(head1)
    print(f"Test 1 Results: {list_to_array(result1)}")

    head2 = build_list([2, 1, 3, 5, 6, 4, 7])
    result2 = sol.reverseList(head2)
    print(f"Test 2 Results: {list_to_array(result2)}")