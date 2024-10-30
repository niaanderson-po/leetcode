class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        lis = [1] * N #initalize to 1 because each will be at least a subsequence of 1 num

        for i in range(N):
            for j in range(i): #compute all ele before i hence in range(i)
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j]) #i understand the visual but not the code for this line, also the purpose of * N in line 4

        lds = [1] * N
        for i in reversed(range(N)): #lost
            for j in range(i + 1, N): #lost
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], 1 + lds[j])

        res = N #lost
        for i in range(1, N - 1): #go through all possible pivots
            if min(lis[i], lds[i]) > 1:
                res = min(
                    res,
                    N - lis[i] - lds[i] + 1
                )#lost

        return res
    
#REVISIT AFTER REVIEWING LIS AND LDS ALGORITHMS