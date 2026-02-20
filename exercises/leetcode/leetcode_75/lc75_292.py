'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        read_s = 0
        read_t = 0

        while read_s < len(s):
            if read_t == len(t):
                return False
            if s[read_s] == t[read_t]:
                read_s += 1
                read_t += 1
            else:
                read_t += 1
        return True

sol = Solution()
print(sol.isSubsequence("abc","ahbgdc"))
print(sol.isSubsequence("axc","ahbgdc"))

# Using an iterator:

class Solution2(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        it = iter(t)

        return all(char in it for char in s)
    
# Follow-up using binary search:

from collections import defaultdict
import bisect

class Solution3(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_to_indices = defaultdict(list)
        for index, char in enumerate(t):
            char_to_indices[char].append(index)

        current_t_index = -1
        for char in s:
            if char not in char_to_indices:
                return False
            
            indices_list = char_to_indices[char]

            index_in_list = bisect.bisect_right(indices_list, current_t_index)

            if index_in_list == len(indices_list):
                return False
            
            current_t_index = indices_list[index_in_list]

        return True
