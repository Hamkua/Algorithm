t = int(input())

for _ in range(t):
  n = int(input())
  arr = [1]*(n+1)

  result = 0
  for i in range(1,n):
    if(i<3):
      arr[i+1] = (arr[i]) + arr[i]
    else:
      arr[i+1] = arr[i] + arr[i-1] + arr[i-2]
      
  print(arr[n])