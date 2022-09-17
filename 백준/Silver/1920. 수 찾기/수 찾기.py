import sys
input = sys.stdin.readline   

n = int(input())
n_data = list(map(int,input().split()))

m = int(input())
m_data = list(map(int,input().split()))

n_data.sort()

def bs(data,target,start,end):
  while start<=end:
    mid = (start+end)//2
    if data[mid] == target:
      return 1
    elif data[mid] > target:
      end = mid-1
    else:
      start = mid+1
  return 0

l = len(n_data)-1

for x in m_data:
  result = bs(n_data, x, 0, l)
  print(result)
