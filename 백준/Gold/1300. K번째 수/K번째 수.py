import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
  
start = 1
end = k

while(start <= end):
  mid = (start + end) // 2 

  cnt = 0
  for i in range(1, n+1):
    cnt += min(n, mid//i)
  
  if(cnt < k):
    start = mid + 1
  elif(cnt >= k):
    result = mid

    end = mid - 1


print(result)