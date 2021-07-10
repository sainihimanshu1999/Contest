'''It is little different from normal decode ways here we have '*' which matches any number form 0to9'''


def decodeWays(s):
    dp = [1,0,0]

    for char in s:
        dp_new = [0,0,0]
        if char == '*':
            dp_new[0] = 9*dp[0] + 9*dp[1] + 6*dp[2]
            dp_new[1] = dp[1]
            dp_new[2] = dp[2]

        else:
            dp_new[0] = (char>'0')*dp[0] + dp[1] + (char<='6')*dp[2]
            dp_new[1] = (char=='1')*dp[0]
            dp_new[2] = (char=='1')*dp[0]

    return dp[0]
