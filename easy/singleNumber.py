"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant 
extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

#Approach: Hash Tables

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict = {}
        for ele in nums:
            if ele not in dict:
                dict[ele] = 1
            else:
                dict[ele] += 1
    
        for ele in dict:
            if dict[ele] == 1:
                return ele
            
#Testing

solution = Solution()
test_cases = [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1)
]

for nums, expected in test_cases:
    result = solution.singleNumber(nums)
    print({f"Input: {nums}, Expected: {expected}, Got: {result}, {'Passed' if result == expected else 'Failed'}"})
