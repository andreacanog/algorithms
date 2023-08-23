# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

## Time Complexity: O(n) bc we are iterating through the array once and the lookup time for hash is O(1)  
## Space Complexity: O(n) bc we are storing the values in the hash table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hash:
                return [hash[diff], i]
            
            hash[n] = i
        
        return 


## Javascript Solution

var twoSum = function(nums, target) {
   let obj = {};

   for (let i = 0; i < nums.length; i++) {
       let num = nums[i]
       let diff = target - num;

       if (diff in obj) return [obj[diff], i]

       obj[num] = i
   }

   return 
};