from collections import deque
import sys
input = sys.stdin.readline
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]

def bfs(x,y,tx,ty):
  if x== tx and y == ty:
    return 0
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx< 0 or ny<0 or nx>=l or ny>=l:
        continue
      if  data[nx][ny] == 0:
        data[nx][ny] = data[x][y] + 1
        queue.append((nx,ny))
  return data[tx][ty]

cnt = int(input().rstrip())
for _ in range(cnt):
  l = int(input().rstrip())    #체스판의 크기 입력받기
  data = [[0]*l for _ in range(l)]
  x,y = map(int,input().split())
  target_x , target_y = map(int,input().split())
  print(bfs(x,y,target_x,target_y))
