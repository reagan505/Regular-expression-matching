def isMatch(s: str, p: str) -> bool:


  dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)] #createted a 2D list with dimensions (len(s) + 1) by (len(p) + 1)
  dp[0][0] = True #An empty string "" matches an empty pattern ""

  for j in range(1, len(p) + 1): #for loop iterating over each position in the pattern p
    if p[j - 1] == '*':
      dp[0][j] = dp[0][j - 2]

  for i in range(1, len(s) + 1):  #starts nested loop to fill in the dp table.
    for j in range(1, len(p) + 1):

      if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
        dp[i][j] = dp[i - 1][j - 1]

      elif p[j - 1] == '*':
        dp[i][j] = dp[i][j - 2]

        if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

  return dp[len(s)][len(p)]

# TEST CASES
s = "aab"

print(isMatch(s))