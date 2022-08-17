import sys
input = sys.stdin.readline

def dfs(start, result):
  for node, edge  in data[start]:
    if result[node] == -1:
      result[node] = result[start] + edge
      dfs(node, result)


v = int(input())
data = [[]  for _ in range(v + 1)]
for _ in range(v):
  tmp = list(map(int, input().strip().split()))

  current_index = tmp[0]
  for i in range(1, len(tmp)//2):
    x = tmp[2 * i - 1]
    y = tmp[2 * i]
    data[current_index].append((x, y))

result = [-1] * (v + 1)
result[1] = 0
dfs(1, result)

index = result.index(max(result))

result = [-1] * (v + 1)
result[index] = 0
dfs(index, result)
result.sort()

print(result.pop())