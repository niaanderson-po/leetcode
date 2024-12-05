"""
Given an array of positive integers nums, return the number of distinct prime factors 
in the product of the elements of nums.

Note that:
A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
 

Example 1:
Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.

Example 2:
Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.
"""

class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        def find_prime_factor(n):
            factors = []
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    while n % i == 0:
                        n //= i
                    factors.append(i)
            if n > 1:
                factors.append(n)
            return factors

        factors = set()
        for n in nums:
            i = find_prime_factor(n)
            for ele in i:
                factors.add(ele)
        
        return len(factors)

        return find_prime_factor(nums)

#Testing
solution = Solution()
test_cases = [
    ([2,4,3,7,10,6], 4),
    ([2,4,8,16], 1)
]

for nums, expected in test_cases:
    result = solution.distinctPrimeFactors(nums)
    print(f"Input: {nums}, Expected: {expected}, Got: {result}, {'Passed' if result == expected else 'Failed'}")