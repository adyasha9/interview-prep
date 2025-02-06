def dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = dp(n-1, memo) + dp(n-2, memo)
    return memo[n]
# 💡 Tip: Convert recursive to iterative (Bottom-Up) for efficiency.

