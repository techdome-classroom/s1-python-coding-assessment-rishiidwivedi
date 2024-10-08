def decode_s( s: str, p: str) -> bool:
    
   m, p = len(s), len(p)
    
    # dp table where dp[i][j] is True if s[0..i-1] matches p[0..j-1]
    dp = [[False] * (p + 1) for _ in range(m + 1)]
    
    # Empty p matches an empty s
    dp[0][0] = True
    
    # If the p starts with '*', it can match an empty s
    for j in range(1, p + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, p + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                # Current characters match, or the p has '?', which matches any one character
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match zero characters (dp[i][j-1]) or one or more characters (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    # The result is stored in dp[m][p], whether the entire s matches the entire p
    return dp[m][p]
  
        return False
