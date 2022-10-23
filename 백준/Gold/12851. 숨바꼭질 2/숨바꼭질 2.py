from collections import deque
import sys 
input = sys.stdin.readline

n,k = map(int,input().split())

visited= [-1]*100001
visited[n]=0

cnt = 0
result = 0

queue = deque()
queue.append(n)

while queue:
  curr_num = queue.popleft()

  if curr_num == k:
    cnt += 1
   
  for i in [curr_num*2, curr_num+1, curr_num-1]:

    if 0<=i<=100000:
      if visited[i] == -1 or visited[i]>=visited[curr_num]+1:
        visited[i] = visited[curr_num]+1
        queue.append(i)
      
print(visited[k])
print(cnt)