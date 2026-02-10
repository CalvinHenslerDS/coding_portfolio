'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        output = ""
        working_divisor = ""
        candidate_divisors = []
        length_str1 = len(str1)
        length_str2 = len(str2)

        for letter in str1:
            working_divisor += letter
            candidate_divisors.append(working_divisor)
        
        for candidate in candidate_divisors:
            candidate_length = len(candidate)
            

#         output = ""
#         candidate_divisor = ""
#         candidate_divisors = []
#         divisor = ""
#         length1 = len(str1)
#         length2 = len(str2)
        
#         for letter1 in str1:
            
#             print(candidate_divisor)
#             if (candidate_divisor[0] == letter1) or (len(candidate_divisor) == len(str1)):
#                 length_divisor = len(candidate_divisor)
#                 print(length_divisor)
#                 remainder1 = length1 % length_divisor

#                 if remainder1 == 0:
#                     print("here")
#                     candidate_repeat_count1 = int(length1 / length_divisor)
#                     #print(candidate_repeat_count1)

#                     if candidate_divisor * candidate_repeat_count1 == str1:
#                         candidate_repeat_count2 = int(length2 / length_divisor)
#                         #print(candidate_divisor)
#                         if candidate_repeat_count2 * candidate_divisor == str2:
#                             candidate_divisors.append(candidate_divisor)
#                             #print("hi")
#                             for i in range(candidate_repeat_count1):
#                                 candidate_divisor = (i + 1) * candidate_divisor
#                                 length_candidate_divisor = len(candidate_divisor)
#                                 candidate_repeat_count1 = int(length1 / length_candidate_divisor)
#                                 candidate_repeat_count2 = int(length2 / length_candidate_divisor)
#                                 validator1 = candidate_repeat_count1 * candidate_divisor
#                                 validator2 = candidate_repeat_count2 * candidate_divisor

#                                 if (validator1 == str1) and (validator2 == str2):
#                                     divisor = candidate_divisor


#                         else:
#                             print(candidate_divisors)
#                             divisor = ""

#                         return divisor
            
            



# sol = Solution()
# print(sol.gcdOfStrings('LEETLEETLEET','LEETLEET'))

#print(f"inputs: 'abc', 'pqr': {sol.mergeAlternately('abc','pqr')}")
#print(f"inputs: 'ab', 'pqrs': {sol.mergeAlternately('ab','pqrs')}")
#print(f"inputs: 'abcd', 'pq': {sol.mergeAlternately('abcd','pq')}")