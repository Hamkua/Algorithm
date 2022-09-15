import sys
input = sys.stdin.readline
  
n = int(input())
temp = [n+1]*n
temp[0] = 0

data = list(map(int,input().split()))

for i in range(n):
  for j in range(1,data[i]+1):
    if i + j >= n:
     break
    temp[i+j] = min(temp[i+j],temp[i]+1)

print(temp[n-1] if temp[n-1]!= n+1 else -1)


