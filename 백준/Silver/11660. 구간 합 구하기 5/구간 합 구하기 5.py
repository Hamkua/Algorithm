import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

data =  [list(map(int, input().strip().split())) for _ in range(n)]
accumulated_data = [[0] * (n + 1) for _ in range(n + 1)]
result = []

for x in range(1,n+1):
  for y in range(1,n+1):
    accumulated_data[x][y] = data[x - 1][y - 1] + accumulated_data[x - 1][y] + accumulated_data[x][y - 1] - accumulated_data[x - 1][y - 1]
  
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().strip().split())
  result.append(accumulated_data[x2][y2] - accumulated_data[x2][y1 - 1] - accumulated_data[x1 - 1][y2] + accumulated_data[x1 - 1][y1 -1])
  
  
#   answer.append(value)
for answer in result:
  print(answer)