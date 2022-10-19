import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

dp = [1]
for i in range(n):
  dp.append((i + 1 )* dp[i])

print(dp[n] // (dp[n - m] * dp[m]))