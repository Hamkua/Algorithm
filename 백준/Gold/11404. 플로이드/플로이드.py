import sys
INF = sys.maxsize
input = sys.stdin.readline 

def floyed():
  for i in range(v):
    for j in range(v):
      for k in range(v):
        if(data[j][k] > data[j][i] + data[i][k]):
          data[j][k] =  data[j][i] + data[i][k]
        
v = int(input())
e = int(input())

data = [[INF] * (v) for _ in range(v)]

for i in range(v):
  data[i][i] = 0
for _ in range(e):
  start, end, w = map(int, input().strip().split())
  start -= 1
  end -= 1

  if(data[start][end] > w):
    data[start][end] = w
  
floyed()

for i in range(v):
  for j in range(v):
    if(data[i][j] == INF):
      print(0, end=" ")
    else:
      print(data[i][j], end=" ")
  print()