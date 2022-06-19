import sys
input = sys.stdin.readline   

t = int(input())
for _ in range(t):
  n = int(input())
  data = list(map(int,input().split()))
  data.sort()

  tmp = []
  temp = []

  diff = 0
  for i in range(n):
    if i%2 == 0:
      tmp.append(data[i])
    else:
      temp.append(data[i])

  for i in range(len(temp)):
    tmp.append(temp[len(temp)-i-1])

  for i in range(n):
    result = abs(tmp[i] - tmp[i-1])
    if diff < result:
      diff = result
  print(diff)