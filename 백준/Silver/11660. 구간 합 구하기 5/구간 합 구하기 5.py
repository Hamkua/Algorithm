import sys
input = sys.stdin.readline
data = []
answer = []

n, m = map(int, input().strip().split())

for _ in range(n):
  data.append(list(map(int, input().strip().split())))

for x in range(n):
  sum_value = 0
  for y in range(n):
    sum_value += data[x][y]
    data[x][y] =sum_value

for i in range(m):
  x1, y1, x2, y2 = map(int, input().strip().split())

  value = 0
  for x in range(x1 - 1, x2):
    if y1 > 1:
      value += data[x][y2 -1] - data[x][y1 - 2]
    else:
      value += data[x][y2 -1]
  
  answer.append(value)

for result in answer:
  print(result)