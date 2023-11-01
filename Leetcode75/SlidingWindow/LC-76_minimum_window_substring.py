# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, 
# return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = 0
        left = 0
        window = defaultdict(int)
        countT = defaultdict(int)

        for char in t:
            countT[char] += 1
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in countT and window[char] == countT[char]:
                have += 1

                while have == need:
                    #update values
                    if (right - left + 1) < resLen:
                        res = [left, right]
                        resLen = right - left + 1
                    #pop from left
                    window[s[left]] -= 1

                    if s[left] in countT and window[s[left]] < countT[s[left]]:
                        have -= 1
                    
                    left += 1
        left, right = res
        return s[left:right + 1] if resLen != float("infinity") else ""
    

# JavaScript 

var minWindow = function(s, t) {
    if (t === "") return ""

    let window = new Map(), countT = new Map();

    for (let char of t) {
        countT.set(char, countT.get(char) + 1 || 1)
    }

    have = 0, need = countT.size
    let res = [-1,-1], resLen = Infinity
    let left = 0
    let right;
    for (right = 0; right < s.length; right++) {
        let char = s[right]
        window.set(char, window.get(char) + 1 || 1)

        if (countT.has(char) && window.get(char) === countT.get(char)) {
            have++;
        }

        while (have === need) {
            //update our results
            if ((right - left + 1) < resLen) {
                resLen = (right - left + 1)
                res = [left, right]
            }
            // pop from the left of the string
            window.set(s[left], window.get(s[left]) - 1)
            if (countT.has(s[left]) && window.get(s[left]) < countT.get(s[left])) {
                have--;
            }
            left++
        }
    }
    console.log(res)
    let [l, r] = res
    return resLen !== Infinity ? s.slice(l, r + 1) : "" 
};