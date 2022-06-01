from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
  visited = [0]*(n+1)
  sum_value = 0
  queue = deque()
  queue.append(x)
    
  while queue:
    q = queue.popleft()
    for i in data[q]:
      if visited[i] == 0 and i != q:
        visited[i] = visited[q]+1
        queue.append(i)
  visited[x] = 0
  for i in range(len(visited)):
    sum_value += int(visited[i])
  result[x]=sum_value

n,m = map(int, input().split())
data = [[] for _ in range(n+1)]
result = [0]*(n+1)
min_index = 101
min_value = 5001

for _ in range(m):  
  a,b = map(int,input().split())
  data[a].append(b)
  data[b].append(a)

for i in range(1,n+1):
  bfs(i)
for i in range(1,n+1):
  if result[i] < min_value:
    min_index = i
    min_value = result[i]
print(min_index)
