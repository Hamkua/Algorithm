import sys

input = sys.stdin.readline

a = []
b = []

n, m = map(int, input().strip().split())

for _ in range(n):
  a.append(list(map(int, input().strip().split())))

n2, m2 = map(int, input().strip().split())

for _ in range(m):
  b.append(list(map(int, input().strip().split())))

c = [[] for _ in range(n)]
# for i in range(n):
#   tmp = 0
#   for j in range(len(a[i])):
#     tmp += a[i][j] * b[j][i]

#   c.append(tmp)

# print(c)


for i in range(n):
  for k in range(m2):
    tmp = 0
    for j in range(m):
      tmp += a[i][j] * b[j][k]

    c[i].append(tmp)
  
for i in range(len(c)):
  for j in range(len(c[i])):
    print(c[i][j], end=" ")

  print()