# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

# Time Complexity: O(nk) where n is the length of strs and k is the length of the longest string in strs
# Space Complexity: O(nk) bc we are storing the values in the hash table

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1

            res[tuple(count)].append(string)
        
        return res.values()



# Javascript Solution
## Time: O(nklogk) where n is the length of strs and k is the length of the longest string in strs

var groupAnagrams = function(strs) {
    let anagramMap = new Map();
    
    for (let str of strs) {
        let currentStr = str.split("").sort().join("");
        if (!anagramMap.has(currentStr)) {
            anagramMap.set(currentStr, [])
        }
        anagramMap.get(currentStr).push(str)
    }

    return Array.from(anagramMap.values());
};