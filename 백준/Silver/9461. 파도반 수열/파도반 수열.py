import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  data = [1,1,1]
  if(n > len(data)):
    for i in range(3, n):
      data.append(data[i - 3] + data[i - 2])

  print(data.pop())