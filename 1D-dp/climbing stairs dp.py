# Climbing Stairs
# Solved 
# You are given an integer n representing the number of steps to reach the top of a staircase. 
# You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

# Example 1:

# Input: n = 2

# Output: 2
# Explanation:

# 1 + 1 = 2
# 2 = 2

#  TOP DOWN 
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1,2:2}
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        return f(n)

# BOTTOM UP
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 or n==2 or n==0:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
# BOTTOM UP OPTIMISED
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 or n==2 or n==0:
            return n
        prev = 1
        curr = 2
        for i in range(3,n+1):
            prev,curr = curr,prev+curr
        return curr
        
