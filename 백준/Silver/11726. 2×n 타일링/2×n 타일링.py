n = int(input())

arr = [0,1,2]
for i in range(n+1):
  if i<3:
    continue
  arr.append(arr[i-2] + arr[i-1])

print(arr[n]%10007)