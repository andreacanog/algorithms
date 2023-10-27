# You are given a string s and an integer k. You can choose any character of the string and change it 
# to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0
        maxS = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxS = max(maxS, count[s[right]])

            while (right - left + 1) - maxS > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res



# /**
#  * @param {string} s
#  * @param {number} k
#  * @return {number}
#  */
# var characterReplacement = function(s, k) {
#     let count = {};
#     let left = 0;
#     let res = 0;
#     let maxS = 0;

#     for (let right = 0; right < s.length; right++) {
#         if (!count[s[right]]) {
#             count[s[right]] = 0
#         }
#         count[s[right]] += 1
#         maxS = Math.max(maxS, count[s[right]])

#         while ((right - left + 1) - maxS > k) {
#             count[s[left]] -= 1;
#             left++
#         }

#         res = Math.max(res, right - left + 1)
#     }
#         return res;
    
# };