import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

cnt = 0
result = 0
end = 0
for i in range(n):
  while result<m and end<n:
    result += data[end]
    end += 1
  if result == m:
    cnt+= 1
  result-=data[i]

print(cnt)