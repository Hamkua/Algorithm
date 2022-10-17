from collections import deque
import sys
input = sys.stdin.readline 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_edges():
  visited = [[0] * m for _ in range(n)]
  edge_list = list()
  queue = deque()
  queue.append((0, 0))
  
  while(queue):
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < n and 0 <= ny < m):
        
        if(visited[nx][ny] == 0):
          visited[nx][ny] = 1
          if(data[nx][ny] != 1):
            queue.append((nx, ny))
        else:
          if(data[nx][ny] == 1):
            edge_list.append((nx, ny))
  
  return edge_list
  
n, m = map(int, input().strip().split())

data = list()
for _ in range(n):
  data.append(list(map(int, input().strip().split())))

result = 0
while(1):
  edge_list = find_edges()
  if(len(edge_list) == 0):
    break

  for x, y in edge_list:
    data[x][y] = 0
  result += 1
print(result)