import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
data = list(map(int, input().split()))

cost = data[0]
result = cost * length[0]

for i in range(1,n-1):
  if cost>data[i]:
    result += data[i]*length[i]
    cost = data[i]
  else:
    result += cost*length[i]

print(result)