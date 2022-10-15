import sys
input = sys.stdin.readline 

a = input().strip()
b = input().strip()

data = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
  for j in range(1, len(b) + 1):
    if(a[i - 1] == b[j - 1]):
      data[i][j] = data[i - 1][j - 1] + 1
    else:
      data[i][j] = max(data[i - 1][j], data[i][j - 1])

result = ""
x, y = len(a), len(b)
while(x > 0 and y > 0):
  if(data[x][y] == data[x - 1][y]):
    x -= 1
  elif(data[x][y] == data[x][y -1]):
    y -= 1
  else:
    result = a[x - 1] + result 
    x -= 1
    y -= 1

length = len(result)
print(length)
if(length != 0):
  print(result)