import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
k = int(input())

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

body = deque([(0,0)])
data = [[0] * n for _ in range(n)]
command = dict()

for _ in range(k):
  x, y = map(int, input().strip().split())
  data[x-1][y-1] = 1

l = int(input())
for _ in range(l):
  s, d = input().strip().split()
  s = int(s)

  command[s] = d


sec = 0
d = 0
while 1:
  sec += 1

  x, y = body[-1]

  # print(sec, x, y, d)
  
  dx, dy = direction[d]
  nx = x + dx
  ny = y + dy

  if (nx, ny) not in body and 0<=nx<n and 0<=ny<n:

  
    body.append((nx, ny))
    if(data[nx][ny] != 1):
      body.popleft()
      
    else:
      data[nx][ny] = 0
    
    if sec in command:
      cmd = command.pop(sec)
      # print(sec, cmd)
      if cmd == "D":
        d += 1
        if d>=4:
          d = 0
  
      else:
        d -= 1
        if d < 0:
          d = 3
  else:
    break

print(sec)