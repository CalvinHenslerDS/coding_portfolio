'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()

        words.reverse()

        result = " ".join(words)

        return result
    
sol = Solution()

print(sol.reverseWords("the sky is blue"))

# O(1) Solution

class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = list(s)
        length = len(l)

        slow = 0
        fast = 0

        while fast < length:
            while fast < length and l[fast] == ' ':
                fast += 1
            if fast < length:
                if slow != 0:
                    l[slow] = ' '
                    slow += 1

                while fast < length and l[fast] != ' ':
                    l[slow] = l[fast]
                    slow += 1
                    fast += 1
        
        l = l[:slow]
        length = len(l)

        self.reverse_segment(l, 0, length -1)

        start = 0
        for end in range(length + 1):
            if end == length or l[end] == ' ':
                self.reverse_segment(l, start, end - 1)
                start = end + 1
        return "".join(l)
    
    def reverse_segment(self, l, left, right):
        '''
        Helper to reverse a portion of the list in-place.

        :type l: list
        :type left: int
        :type right: int
        '''
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

sol = Solution2()

print(sol.reverseWords("the sky is blue"))