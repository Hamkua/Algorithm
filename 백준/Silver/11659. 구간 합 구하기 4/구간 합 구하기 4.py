import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
data = list(map(int, input().strip().split()))

result = [0]
for i in range(n):
  result.append(result[i] + data[i])
for _ in range(m):
  a, b = map(int, input().strip().split())
  print(result[b] - result[a - 1])