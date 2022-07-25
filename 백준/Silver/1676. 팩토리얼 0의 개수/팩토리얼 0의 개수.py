n = int(input())
f = n
while(n > 1):
  n -= 1
  f *= n

f = str(f)
result = 0
while(len(f) > 1 and f[-1] == "0"):
  f = f[:-1]
  result += 1

print(result)