def longestConsecutive(nums) -> int:
    if len(nums) == 0:
        return 0
    def f(i):
        if nums[i]-1 not in s:
            visited[i] = True
            dp[i] = 1;
            return dp[i]
        dp[i] = 1 + f(s[nums[i] - 1])
        visited[i] = True
        return dp[i]
    
    s = dict()
    for i in range(len(nums)):
        s[nums[i]] = i
    n = len(nums)
    dp = [0] * n
    visited = [False] * n
    # define dp[i] := length of longest consecutive sequence that ends at a[i]
    # dp[i] = dp[s[nums[i]-1]]
    for i in range(n):
        if visited[i] == True:
            continue
        f(i)
    return max(dp)