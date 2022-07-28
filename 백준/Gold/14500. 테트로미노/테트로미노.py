import sys
from collections import deque 
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,cnt,result,visited):
  global max_result
  if(cnt > 1):
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0<=nx<n and 0<=ny<m):
        if(nx, ny) not in visited:
          dfs(nx, ny, cnt - 1, result + data[nx][ny], visited + [(nx,ny)])
          dfs(x, y, cnt - 1, result + data[nx][ny], visited + [(nx,ny)])
  else:
    # print()
    # tmp = [[0]*m for _ in range(n)]
    # for a,b in visited:
    #   tmp[a][b] = 1
    # for i in range(n):
    #   print(tmp[i])
    # print(result)
    max_result = max(max_result, result)


n,m = map(int, input().strip().split())
data = []
for _ in range(n):
  data.append(list(map(int, input().strip().split())))


max_result = 0
for i in range(n):
  for j in range(m):
    dfs(i,j,4,data[i][j],[(i,j)])
    
print(max_result)
