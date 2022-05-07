import sys
input = sys.stdin.readline

n,x,y = map(int,input().split())
result = 0

while(n):
  n -= 1
  if (x < 2**(n) and y < 2**(n)):
    continue

  elif (x < 2**(n) and y >= 2**(n)):
    result += (2**(n) * 2**(n))
    y -= 2**(n)

  elif(x >= 2**(n) and y < 2**(n)):
    result +=  (2**(n) * 2**(n))*2
    x -= 2**(n)

  elif(x >= 2**(n) and y >= 2**(n)):
    result += (2**(n) * 2**(n))*3
    x -= 2**(n)
    y -= 2**(n)

print(result)