import sys
from collections import deque

input = sys.stdin.readline
f,s,g,u,d = map(int,input().split())
visited = [-1]*(f+1)
visited[s] = 0

queue = deque()
queue.append(s)
result = False
while queue:
  curr = queue.popleft()
  if curr == g:
    result = True
    break

  for i in (curr+u, curr-d):
    if 0<i<=f:
      if visited[i]==-1:
        visited[i] = visited[curr]+1
        queue.append(i)

if result == False:
  print("use the stairs")
else:
  print(visited[g])