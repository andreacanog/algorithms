# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Time: O(n) bc we loop through s and t once each (2n) 
## Space: O(n) bc we used a hashmap to store the count of each character in s and t (2n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True



# JavaScript Solution

## Time: O(n) bc we loop through s and t once each (2n)
## Space: O(n) bc we used a hashmap to store the count of each character in s and t (2n)

var isAnagram = function(s, t) {
    if (s.length != t.length) return false;

    const count = {};
    const length = s.length;

    for (let i = 0; i < length; i++) {
        if (!count[s[i]]) count[s[i]] = 0;
        if (!count[t[i]]) count[t[i]] = 0;

        count[s[i]]++
        count[t[i]]--
    }

    for (let char in count) {
        if (count[char] !== 0) return false;
    }

    return true;
};
