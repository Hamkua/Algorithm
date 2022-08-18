import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(start, result):

  for child, edge in data[start]:
    if result[child] == -1:
      result[child] = result[start] + edge
      dfs(child, result)
    

n = int(input())
data = [[] for _ in range(n + 1)]

for _ in range(n - 1):
  parent, child, edge = map(int, input().strip().split())
  data[parent].append((child, edge))
  data[child].append((parent, edge))


result = [-1] * (n + 1)
result[1] = 0

dfs(1, result)

start = result.index(max(result))

result = [-1] * (n + 1)
result[start] = 0

dfs(start, result)

result.sort()
print(result.pop())