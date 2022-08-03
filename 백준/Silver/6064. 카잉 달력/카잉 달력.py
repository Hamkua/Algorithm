import sys
input = sys.stdin.readline 

t = int(input())

for _ in range(t):
  m, n, x, y = map(int, input().strip().split())
  bool = False
  while(x <= m*n):
    
    if ((x - y) % n == 0):
      print(x)
      bool = True
      break
    x += m

  if bool == False:
    print(-1)