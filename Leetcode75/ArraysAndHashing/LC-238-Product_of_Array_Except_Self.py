# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

## time complexity: O(n)
## space complexity: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1

        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        post = 1

        for i in range(len(res) -1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res


## JS solution 
## time complexity: O(n)
## space complexity: O(1)

var productExceptSelf = function(nums) {
    let res = [];
    let pre = 1;

    for (let i = 0; i < nums.length; i++) {
        res[i] = pre;
        pre *= nums[i]
    }

    post = 1;

    for (let i = res.length - 1; i >= 0; i--) {
        res[i] *= post;
        post *= nums[i]
    }

    return res
};