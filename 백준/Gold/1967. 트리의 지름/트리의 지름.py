from collections import deque

n=int(input())
tree={i:[] for i in range(n+1)}
for i in range(n-1):
  a,b,weight=map(int, input().split())
  tree[a].append((b,weight))
  tree[b].append((a,weight))

def bfs(s):
  queue=deque()
  queue.append((s,0))
  visited=[0]*n
  visited[s-1]=1

  result=[0,0]
  while queue:
    now,cnt=queue.popleft()
    for i in tree[now]:
      next_number,value=i[0],i[1]
      if visited[next_number-1]==0:
        visited[next_number-1]=1
        queue.append((next_number,cnt+value))
        if result[1]<cnt+value:
          result[0]=next_number
          result[1]=cnt+value

  return result

a=bfs(1)
b=bfs(a[0])
print(b[1])