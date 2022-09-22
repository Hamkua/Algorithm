import sys
input = sys.stdin.readline   

def bs(arr,target,start,end):

  while start<=end:
    mid = (start + end)//2
    result = 0
    for i in arr:
      if i <= mid:
        continue
      else:
        result += (i - mid)
    if result < target:
      end = mid - 1
    elif result >= target:
      start = mid + 1
  return end
        
n,m = map(int,input().split())
data = list(map(int,input().split()))

result = bs(data,m,0,max(data))
print(result)