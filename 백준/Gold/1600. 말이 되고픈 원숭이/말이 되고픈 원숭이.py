from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -2, -2, -1, 1, 2, 2, -1, 1]
dy = [0, 0, -1, 1, -1, 1, -2, -2, -1, 1, 2, 2]

def bfs(k):
  queue = deque()
  queue.append((0, 0, k))
  visited[0][0][k] = 0

  while(queue):
    x, y, k = queue.popleft()
    for i in range(len(dx)):
      if i > 3 and k == 0:
        continue
      
      nx = x + dx[i]
      ny = y + dy[i]

      if(0 <= nx < h and 0 <= ny < w):
        if(data[nx][ny] == 0):
          # 이전의 k를 어떻게 알아낼 것인가 ? 
          
          if(i > 3 and  k - 1 not in visited[nx][ny]):
            queue.append((nx, ny, k - 1))
            visited[nx][ny][k - 1] = visited[x][y][k] + 1
            # for i in range(h):
            #   print(visited[i])
            # print()
            

          elif(i <= 3 and k not in visited[nx][ny]):
            queue.append((nx, ny, k))
            visited[nx][ny][k] = visited[x][y][k] + 1
            # for i in range(h):
            #   print(visited[i])
            # print()
          
          
k = int(input())
w, h = map(int, input().strip().split())
visited = [[dict() for i in range(w)] for _ in range(h)]

data = list()
for _ in range(h):
  data.append(list(map(int, input().strip().split())))

bfs(k)


result = visited[h - 1][w - 1].values()
if(len(result) == 0):
  print(-1)
else:
  print(min(result))