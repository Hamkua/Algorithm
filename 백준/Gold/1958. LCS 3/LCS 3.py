import sys
input = sys.stdin.readline 

a = input().strip()
b = input().strip()
c = input().strip() 

data = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
  for j in range(1, len(b) + 1):
    for k in range(1, len(c) + 1):
      if(a[i - 1] == b[j - 1] == c[k - 1]):
        data[i][j][k] = data[i - 1][j - 1][k - 1] + 1
      else:
        data[i][j][k] = max(data[i - 1][j][k], data[i][j - 1][k], data[i][j][k - 1])

result = ""
x, y, z = len(a), len(b), len(c)
while(x > 0 and y > 0 and z > 0):
  if(data[x][y][z] == data[x - 1][y][z]):
    x -= 1
  elif(data[x][y][z] == data[x][y - 1][z]):
    y -= 1
  elif(data[x][y][z] == data[x][y][z - 1]):
    z -= 1
  else:
    result = a[x - 1] + result
    x -= 1
    y -= 1
    z -= 1

print(len(result))