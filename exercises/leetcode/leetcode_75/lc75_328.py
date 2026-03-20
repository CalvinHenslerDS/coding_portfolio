'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
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
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head:
            return None
        
        odd = head
        even = head.next
        even_head = even # Save this to connect at the end
        
        while even and even.next:
            # Link odd to the next odd node
            odd.next = even.next
            odd = odd.next
            
            # Link even to the next even node
            even.next = odd.next
            even = even.next
            
        # Stitch the two lists together
        odd.next = even_head
        return head
    
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
    result1 = sol.oddEvenList(head1)
    print(f"Test 1 Results: {list_to_array(result1)}")

    head2 = build_list([2, 1, 3, 5, 6, 4, 7])
    result2 = sol.oddEvenList(head2)
    print(f"Test 2 Results: {list_to_array(result2)}")