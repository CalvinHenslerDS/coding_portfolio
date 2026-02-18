'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
'''

# Wrong space, but functional:

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        character_count = 0
        character_count_1s = 0
        character_count_10s = 0
        character_count_100s = 0
        character_count_1000s = 0
        last_character = ""
        current_character = ""
        s = []

        for index, character in enumerate(chars):
            if current_character == "":
                current_character = character
            if (character != current_character) or (index == len(chars) - 1):
                if (index == len(chars) - 1) and character != current_character:
                    last_character = character
                if (index == len(chars) - 1) and character == current_character:
                    character_count += 1
                if character_count > 0:
                    s.append(current_character)
                    current_character = character
                if 1 < character_count <= 9:
                    s.append(str(character_count))
                if 10 <= character_count <= 99:
                    character_count_10s = str(character_count // 10)
                    character_count_1s = str(character_count % 10)
                    s.append(character_count_10s)
                    s.append(character_count_1s)
                if 100 <= character_count <= 999:
                    character_count_100s = str(character_count // 100)
                    character_count_10s = str((character_count % 100) // 10)
                    character_count_1s = str(character_count % 100)
                    s.append(character_count_100s)
                    s.append(character_count_10s)
                    s.append(character_count_1s)
                if 1000 <= character_count <= 9999:
                    character_count_1000s = str(character_count // 1000)
                    character_count_100s = str((character_count % 1000) // 100)
                    character_count_10s = str((character_count % 100) // 10)
                    character_count_1s = str(character_count % 1000)
                    s.append(character_count_1000s)
                    s.append(character_count_100s)
                    s.append(character_count_10s)
                    s.append(character_count_1s)
                character_count = 1
                if last_character != "":
                    s.append(last_character)
            else:
                character_count += 1

            #print(character)
            #print(current_character)
            #print(character_count)
        
        return s


sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))
print(sol.compress(["a"]))
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

# To use the correct space, write in place:

class Solution2(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count the occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write