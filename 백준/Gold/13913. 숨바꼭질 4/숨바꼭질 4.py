from collections import deque 
import sys

input = sys.stdin.readline  


n,m = map(int, input().split())
count = 0
queue = deque()
queue.append((n,count))

max_cnt = 100001
visited = [False]*max_cnt 
visited[n] = True
how = [-1]*max_cnt
result = []

while queue:
  curr_n, count = queue.popleft() 

  if curr_n == m:
    
    print(count)
    result.append(curr_n)
    a=how[curr_n]

    while a!=-1:
      result.append(a)
      a = how[a]
    result.reverse()
    print(*result)
    break
  
  for i in (curr_n+1,curr_n-1,2*curr_n):
    if 0<=i<max_cnt:
      if visited[i] == False:
        visited[i]=True 
        how[i] = curr_n
        queue.append((i,count+1))