import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global visited

  if x + 1 == m and y + 1 == n:
    return 1

  elif visited[x][y] != -1:
    return visited[x][y]
    

  way = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    
    if(0<=nx<m and 0<=ny<n):
      if(data[x][y] > data[nx][ny]):
        way += dfs(nx, ny)

  visited[x][y] = way
  return way

m, n = map(int, input().strip().split())

data = []
visited = [[-1] * n for _ in range(m)]
for _ in range(m):
  data.append(list(map(int, input().strip().split())))

result = 0
print(dfs(0,0))