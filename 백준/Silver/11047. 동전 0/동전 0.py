import sys 
input = sys.stdin.readline

n,k = map(int, input().strip().split())
coin = []
for _ in range(n):
  coin.append(int(input()))

result = 0
for _ in range(n):
  value = coin.pop()
  if(k // value) > 0:
    result += (k // value)
    k%=value

print(result)