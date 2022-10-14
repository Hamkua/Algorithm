import sys
input = sys.stdin.readline 

dx = [-1, 0]
dy = [0, -1]
  
a = input().strip()
b = input().strip()

data = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
  for j in range(1, len(b) + 1):
    if(a[i - 1] == b[j - 1]):
      data[i][j] = data[i-1][j - 1] + 1
    else:
      data[i][j] = max(data[i- 1][j], data[i][j - 1])

# for x in range(len(a) + 1):
#   for y in range(len(b) + 1):
#     print(data[x][y], end="\t")
#   print()

# time.sleep(1)
cnt = 0

x, y = len(a), len(b)
while(x > 0 and y > 0):

  if(data[x - 1][y] == data[x][y]):
    x -= 1
  elif(data[x][y - 1] == data[x][y]):
    y -= 1
  else:
    x -= 1 
    y -= 1
    cnt += 1
print(cnt)