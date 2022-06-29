import sys
from collections import deque

input = sys.stdin.readline
max_size = 100001

visited = [False]*max_size
n, m = map(int, input().strip().split())

queue = deque()
visited[n] = True
queue.append((n, 0))

while(queue):
  current, time = queue.popleft()
  if(current == m):
    print(time)
    break
    
  if(0<= current * 2 < max_size):
    if(visited[current * 2] == False):
      visited[current * 2] = True
      queue.appendleft((current * 2, time))

  if(0<=current + 1 < max_size):
    if(visited[current + 1] == False):
      visited[current + 1] = True
      queue.append((current + 1, time + 1))

  if(0<= current - 1 < max_size):
    if(visited[current - 1] == False):
      visited[current - 1] = True
      queue.append((current - 1, time + 1))