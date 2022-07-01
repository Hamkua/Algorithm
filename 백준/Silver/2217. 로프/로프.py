import sys
input = sys.stdin.readline 

n = int(input())
data = []

for _ in range(n):
  data.append(int(input()))
data.sort()

result = data[0]*n
for i in range(1,len(data)):

  if result < data[i]*(n-i):
    result = data[i]*(n-i)
    
print(result)

