import sys
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
  n = int(input())
  data = []
  for i in range(n):
    data.append(list(map(int,input().split())))
  
  data.sort()
  
  cnt = 1
  for i in range(1,n):
    if data[i][1]<data[0][1]:
      data[0][1] = data[i][1]
      cnt+=1
  print(cnt)
