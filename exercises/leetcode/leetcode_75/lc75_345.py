'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u')
        s_vowels = ''
        output = ''

        for character in s[::-1]:
            if character in vowels:
                s_vowels += character
        for character in s:
            if character not in vowels:
                output += character
            else:
                output  += s_vowels[0]
                s_vowels = s_vowels[1:]
        return output

sol = Solution()
print(sol.reverseVowels("IceCreAm"))
print(sol.reverseVowels("leetcode"))