from collections import deque

def visited_check(x,y):
  if visited[x][y] == True:
    return False
  else:
    visited[x][y] = True
    return True
    
maxa,maxb,maxc = map(int, input().split())
visited = [[False]*(maxb+1) for _ in range(maxa+1)]
result = []

cnt = 0
queue = deque()
queue.append((0,0,maxc))


while(queue):
  a,b,c = queue.popleft()
  if(a == 0 and c not in result):
    result.append(c)


  if(maxa - a >= c):
    if(visited_check(a+c, b)):
      queue.append((a + c, b, 0))
  elif(maxa - a < c):
    if(visited_check(maxa, b)):
      queue.append((maxa, b, c - (maxa - a)))

  if(maxb - b >= c):
    if(visited_check(a, b + c)):
      queue.append((a, b+c, 0))
  elif(maxb - b < c):
    if(visited_check(a, maxb)):
      queue.append((a, maxb, c - (maxb - b)))

  if(maxa - a >= b):
    if(visited_check(a+b, 0)):
      queue.append((a + b, 0, c))
  elif(maxa - a < b):
    if(visited_check(maxa, b - (maxa - a))):
      queue.append((maxa, b-(maxa - a), c))

  if(maxc - c >= b):
    if(visited_check(a, 0)):
      queue.append((a, 0, c + b))
  elif(maxc - c < b):
    if(visited_check(a, b - (maxc - c))):
      queue.append((a, b - (maxc - c), maxc))
      
  if(maxb - b >= a):
    if(visited_check(0, b + a)):
      queue.append((0, b + a, c))
  elif(maxb - b < a):
    if(visited_check(a - (maxb - b), maxb)):
      queue.append((a - (maxb - b), maxb, c))

  if(maxc - c >= a):
    if(visited_check(0, b)):
      queue.append((0, b, c + a))
  elif(maxc - c < a):
    if(visited_check()):
      queue.append((a - (maxc - c), b, maxc))

result.sort()
for i in result:
  print(i, end = " ")