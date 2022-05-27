from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int, input().split())
max_num = 100001
visited = [False]*max_num
cnt = 0
queue = deque()

queue.append((n,cnt))
while queue:
  curr_num, count = queue.popleft()

  if curr_num == k:
    print(count)
    break

  temp = curr_num*2
  if 0<=temp<max_num:
    if visited[temp]==False:
      visited[temp] = True
      queue.appendleft((temp, count))

  temp = curr_num+1
  if 0<=temp<max_num:
    if visited[temp]==False:
      visited[temp] = True
      queue.append((temp, count + 1))

  temp = curr_num-1
  if 0<=temp<max_num:
    if visited[temp]==False:
      visited[temp] = True
      queue.append((temp, count + 1))