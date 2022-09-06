import sys
input = sys.stdin.readline

result = 0
n = int(input())
data = []
for _ in range(n):
  data.append(int(input()))
  
data.sort(reverse=True) 

left_set = set()
for x in range(n):
  for y in range(n):
    left_set.add(data[x] + data[y])

for k in range(len(data)):
  for z in range(len(data)):
    if (data[k] - data[z]) in left_set:
      print(data[k])
      exit()