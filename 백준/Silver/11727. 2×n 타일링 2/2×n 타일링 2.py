n = int(input())
result = [0,1,3]
for i in range(n+1):
  if 3 <= i:
    result.append((result[i-2]*2 + result[i-1])%10007)
print(result[n])